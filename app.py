from flask import Flask, render_template, request
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pakar', methods=['GET', 'POST'])
def pakar():
    hasil_pakar = None
    if request.method == 'POST':
        ans = {f"P{i}": request.form.get(f"q{i}") for i in range(1, 16)}

        kesimpulan_data = [
            {
                "id": 1,
                "nama": "POLA TIDUR IDEAL",
                "syarat": {"P4": "t", "P6": "y", "P10": "t", "P15": "t"},
                "durasi": "22.00 - 06.00 (8 Jam)",
                "keterangan": "Pola tidurmu sudah sangat baik. Pertahankan konsistensi jam tidur dan bangun setiap hari, termasuk di akhir pekan."
            },
            {
                "id": 2,
                "nama": "EARLY BIRD TERSTRUKTUR",
                "syarat": {"P1": "y", "P2": "t", "P5": "t", "P15": "t"},
                "durasi": "21.30 - 05.30 (8 Jam)",
                "keterangan": "Kamu cocok dengan pola tidur lebih awal karena aktivitasmu dimulai di pagi hari. Hindari begadang agar energi tetap optimal."
            },
            {
                "id": 3,
                "nama": "NIGHT OWL TERKENDALI",
                "syarat": {"P3": "y", "P4": "t", "P10": "t", "P11": "t"},
                "durasi": "00.00 - 07.00 (7 Jam)",
                "keterangan": "Pola malammu masih terkendali. Pastikan tetap mendapat minimal 7 jam tidur dan hindari penggunaan gadget berlebihan sebelum tidur."
            },
            {
                "id": 4,
                "nama": "KURANG TIDUR KRONIS",
                "syarat": {"P2": "y", "P4": "y", "P10": "y", "P15": "y"},
                "durasi": "23.00 - 06.00 + Tidur Siang (30 Menit)",
                "keterangan": "Kamu mengalami kurang tidur kronis. Mulai kurangi begadang secara bertahap, tetapkan jam tidur konsisten, dan manfaatkan power nap."
            },
            {
                "id": 5,
                "nama": "GANGGUAN POLA TIDUR",
                "syarat": {"P11": "y", "P12": "y", "P14": "y", "P7": "y"},
                "durasi": "22.00 - 06.00 + Perubahan Kebiasaan",
                "keterangan": "Kualitas tidurmu terganggu oleh stres/kebiasaan. Kurangi layar HP 1 jam sebelum tidur, lakukan relaksasi, dan kelola stres."
            }
        ]

        skor_tertinggi = -1
        hasil_terpilih = None

        for k in kesimpulan_data:
            skor = 0
            for tanya, jawab_ideal in k["syarat"].items():
                if ans[tanya] == jawab_ideal:
                    skor += 1

            if skor > skor_tertinggi:
                skor_tertinggi = skor
                hasil_terpilih = k

        if skor_tertinggi == 0:
            hasil_pakar = {
                "nama": "POLA TIDUR CAMPURAN",
                "durasi": "22.30 - 06.00 (7.5 Jam)",
                "keterangan": "Pola tidurmu bervariasi. Usahakan untuk mulai membangun jam tidur yang konsisten setiap malam dan hindari kafein setelah jam 6 sore."
            }
        else:
            hasil_pakar = {
                "nama": hasil_terpilih["nama"],
                "durasi": hasil_terpilih["durasi"],
                "keterangan": hasil_terpilih["keterangan"]
            }

    return render_template('pakar.html', hasil=hasil_pakar)

@app.route('/fuzzy', methods=['GET', 'POST'])
def fuzzy_route():
    hasil_fuzzy = None
    grafik_base64 = None

    if request.method == 'POST':
        v_fisik = int(request.form['fisik'])
        v_mental = int(request.form['mental'])
        v_pengganggu = int(request.form['pengganggu'])

        fisik = ctrl.Antecedent(np.arange(0, 101, 1), 'fisik')
        mental = ctrl.Antecedent(np.arange(0, 101, 1), 'mental')
        pengganggu = ctrl.Antecedent(np.arange(0, 101, 1), 'pengganggu')
        jam_tidur = ctrl.Consequent(np.arange(4, 13, 1), 'jam_tidur') 

        fisik['ringan'] = fuzz.trapmf(fisik.universe, [0, 0, 30, 50])
        fisik['sedang'] = fuzz.trimf(fisik.universe, [30, 50, 70])
        fisik['berat'] = fuzz.trapmf(fisik.universe, [50, 70, 100, 100])

        mental['rendah'] = fuzz.trapmf(mental.universe, [0, 0, 30, 50])
        mental['sedang'] = fuzz.trimf(mental.universe, [30, 50, 70])
        mental['tinggi'] = fuzz.trapmf(mental.universe, [50, 70, 100, 100])

        pengganggu['rendah'] = fuzz.trapmf(pengganggu.universe, [0, 0, 30, 50])
        pengganggu['sedang'] = fuzz.trimf(pengganggu.universe, [30, 50, 70])
        pengganggu['tinggi'] = fuzz.trapmf(pengganggu.universe, [50, 70, 100, 100])

        jam_tidur['kurang'] = fuzz.trapmf(jam_tidur.universe, [4, 4, 5, 7])
        jam_tidur['ideal'] = fuzz.trimf(jam_tidur.universe, [6, 8, 10])
        jam_tidur['ekstra'] = fuzz.trapmf(jam_tidur.universe, [9, 10, 12, 12])

        aturan1 = ctrl.Rule(fisik['berat'] | mental['tinggi'], jam_tidur['ekstra'])
        aturan2 = ctrl.Rule(fisik['sedang'] & mental['sedang'], jam_tidur['ideal'])
        aturan3 = ctrl.Rule(pengganggu['tinggi'], jam_tidur['kurang'])
        aturan4 = ctrl.Rule(fisik['ringan'] & mental['rendah'] & pengganggu['rendah'], jam_tidur['ideal'])

        sistem_tidur = ctrl.ControlSystem([aturan1, aturan2, aturan3, aturan4])
        simulasi = ctrl.ControlSystemSimulation(sistem_tidur)

        simulasi.input['fisik'] = v_fisik
        simulasi.input['mental'] = v_mental
        simulasi.input['pengganggu'] = v_pengganggu
        simulasi.compute()

        hasil_angka = round(simulasi.output['jam_tidur'], 1)

        if hasil_angka >= 9.5: status = "Tidur Ekstra (Recovery)"
        elif hasil_angka >= 6.5: status = "Tidur Ideal (Sehat)"
        else: status = "Waspada Kurang Tidur"

        hasil_fuzzy = {"angka": hasil_angka, "status": status}

        plt.clf()
        jam_tidur.view(sim=simulasi)

        img = io.BytesIO()
        plt.savefig(img, format='png', bbox_inches='tight')
        img.seek(0)
        grafik_base64 = base64.b64encode(img.getvalue()).decode()
        plt.close()

    return render_template('fuzzy.html', hasil=hasil_fuzzy, grafik=grafik_base64)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
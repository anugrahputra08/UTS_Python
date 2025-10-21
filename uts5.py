import os, csv, json, logging, traceback, datetime
from pathlib import Path

# Konfigurasi Folder & File 
DATA_DIR = Path("data")
CSV_PATH = DATA_DIR / "presensi.csv"
JSON_PATH = DATA_DIR / "ringkasan.json"
LOG_PATH = DATA_DIR / "app.log"

DATA_DIR.mkdir(parents=True, exist_ok=True)

# Logging Sederhana 
logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

#  Fungsi Menulis CSV
def tulis_csv(path):
    print("\n=== Input Data Mahasiswa ===")
    try:
        jml = int(input("Masukkan jumlah mahasiswa: "))
        data = []
        for i in range(jml):
            print(f"\nData ke-{i+1}")
            nim = input("NIM: ")
            nama = input("Nama: ")
            hadir = input("Hadir UTS (1=hadir, 0=tidak): ")
            data.append([nim, nama, hadir])

        with open(path, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["nim", "nama", "hadir_uts"])
            writer.writerows(data)

        logging.info("Sukses menulis CSV.")
        print("\n✅ Data berhasil disimpan ke presensi.csv")
    except Exception as e:
        logging.error(f"Gagal menulis CSV: {e}")
        print("❌ Terjadi kesalahan saat menulis CSV:", e)

# Fungsi Membaca CSV dan Simpan Ringkasan JSON 
def baca_dan_ringkas(path):
    try:
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        total = len(rows)
        hadir = sum(1 for r in rows if r["hadir_uts"] == "1")
        persen = round((hadir / total * 100) if total else 0, 2)

        ringkasan = {
            "total": total,
            "hadir": hadir,
            "persentase_hadir": persen,
            "tanggal_diproses": datetime.datetime.now().isoformat(),
            "data": rows
        }

        with open(JSON_PATH, "w", encoding="utf-8") as jf:
            json.dump(ringkasan, jf, indent=2, ensure_ascii=False)

        logging.info("Sukses membuat ringkasan JSON.")
        print("\n📊 Ringkasan disimpan ke ringkasan.json")
        print(f"Total: {total}, Hadir: {hadir}, Persentase: {persen}%")

    except Exception as e:
        logging.error(f"Gagal membaca CSV: {e}")
        print("❌ Terjadi kesalahan saat membaca/meringkas CSV:", e)

# Program Utama 
if _name_ == "_main_":
    logging.info("Program dimulai.")
    try:
        tulis_csv(CSV_PATH)
        baca_dan_ringkas(CSV_PATH)
        logging.info("Program selesai dengan sukses.")
    except Exception as e:
        logging.error(f"Program gagal: {e}")
        print("❌ Program gagal dijalankan.")

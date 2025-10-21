import os
import csv
import json
import logging

# Konfigurasi logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)

try:
    logging.info("Program dimulai...")

    # 1. Membuat folder data
    os.makedirs("data", exist_ok=True)

    # 2. Menulis file CSV
    with open("data/presensi.csv", mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["nim", "nama", "hadir_uts"])
        writer.writerow(["230101001", "anugrah", 1])
        writer.writerow(["230101002", "hanif", 0])
        writer.writerow(["230101003", "bagas", 1])
        writer.writerow(["230101003", "yoma", 0])
        writer.writerow(["230101003", "desta", 1])
    logging.info("File presensi.csv berhasil dibuat.")

    # 3. Membaca kembali CSV dan menghitung ringkasan
    with open("data/presensi.csv", mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)

    total = len(data)
    hadir = sum(int(row["hadir_uts"]) for row in data)
    persentase = (hadir / total) * 100

    ringkasan = {
        "total_mahasiswa": total,
        "hadir": hadir,
        "persentase_hadir": persentase
    }

    # Simpan ke JSON
    with open("data/ringkasan.json", mode="w", encoding="utf-8") as f:
        json.dump(ringkasan, f, indent=4)
    logging.info("File ringkasan.json berhasil disimpan.")

    logging.info("Program selesai dengan sukses.")

except Exception as e:
    logging.error(f"Terjadi kesalahan: {e}")
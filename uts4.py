def jadwal_hari(hari):
    # Data jadwal disimpan dalam dictionary
    jadwal = {
        "senin": ["Bahasa inggris", "Matematika Dasar"],
        "selasa": ["Basis Data", "Algoritma"],
        "rabu": ["Desain Web", "Statistika"],
        "kamis": ["Kecerdasan Buatan", "Pemrograman Visual"],
        "jumat": ["Pemrograman Web"]
    }

    # Ubah input ke huruf kecil agar pencarian tidak sensitif terhadap kapital
    hari = hari.lower()

    # Mengecek apakah hari ada di jadwal
    if hari in jadwal:
        print(f"Jadwal hari {hari.capitalize()}: {jadwal[hari]}")
    else:
        print("Hari tidak ditemukan dalam jadwal.")

# Program utama
hari_input = input("Masukkan nama hari: ")
jadwal_hari(hari_input)

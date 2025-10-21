# Meminta tiga input dari pengguna
setoran1 = int(input("Masukkan setoran pertama: "))
setoran2 = int(input("Masukkan setoran kedua: "))
setoran3 = int(input("Masukkan setoran ketiga: "))

# Mengecek apakah ada input yang tidak valid
if setoran1 <= 0 or setoran2 <= 0 or setoran3 <= 0:
    print("Input tidak valid.")
else:
    # Menjumlahkan semua setoran
    total = setoran1 + setoran2 + setoran3
    print("Total setoran:", total)

    # Menentukan kategori total setoran
    if total < 300000:
        print("Kategori: Rendahh")
    elif total < 600000:
        print("Kategori: Sedang")
    else:
        print("Kategori: Tinggi")

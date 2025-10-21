tarif_dasar = {
    "jakarta": 10000,
    "bandung": 15000,
    "surabaya": 20000
}

def hitung_ongkir(berat_kg, kota, asuransi=False):
    """
    Menghitung ongkos kirim berdasarkan kota, berat, dan opsi asuransi.
    """
    if kota not in tarif_dasar:
        return "Kota tidak terdaftar."

    ongkir = tarif_dasar[kota] + (2000 * berat_kg)
    if asuransi:
        ongkir += 3000
    return ongkir


kota1 = "surabaya"
berat1 = 25
total1 = hitung_ongkir(berat1, kota1)
print("=== Contoh 1 ===")
print(f"Kota Tujuan   : {kota1}")
print(f"Berat Paket   : {berat1} kg")
print(f"Asuransi      : Tidak")
print(f"Total Ongkir  : Rp {total1}")
print()


kota2 = "bandung"
berat2 = 20
total2 = hitung_ongkir(berat2, kota2, True)
print("=== Contoh 2 ===")
print(f"Kota Tujuan   : {kota2}")
print(f"Berat Paket   : {berat2} kg")
print(f"Asuransi      : Ya")
print(f"Total Ongkir  : Rp {total2}")

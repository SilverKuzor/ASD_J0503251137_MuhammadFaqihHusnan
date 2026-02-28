#==================================================
# Nama  : Muhammad Faqih Husnan
# NIM   : J0403251137
# Kelas : B2 TPL
#==================================================
# Latihan 3: Mencari Nilai Maksimum dengan Rekursi

def cari_maks(data, index=0):

    # Kondisi berhenti: ketika mencapai elemen terakhir
    if index == len(data) - 1:
        return data[index]

    # Kondisi rekursif: ambil nilai maksimum dari elemen berikutnya
    maks_sisa = cari_maks(data, index + 1)

    # Tentukan mana yang lebih besar antara elemen saat ini vs maksimum sisa
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa


angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))


# ==========================
# Penjelasan:
# Fungsi memanggil dirinya hingga mencapai elemen terakhir,
# kemudian hasil dikembalikan sambil membandingkan setiap elemen.

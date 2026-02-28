#==================================================
# Nama  : Muhammad Faqih Husnan
# NIM   : J0403251137
# Kelas : B2 TPL
#==================================================
# Latihan 4: Kombinasi Huruf (Backtracking Dasar)

def kombinasi(n, hasil=""):

    # Kondisi berhenti: jika string hasil sudah mencapai panjang n
    if len(hasil) == n:
        print(hasil)
        return

    # Memilih karakter dan melanjutkan eksplorasi
    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")


kombinasi(2)


# ==========================
# Penjelasan:
# Setiap posisi mempunyai 2 pilihan alternatif (A atau B).
# Banyaknya kombinasi yang dihasilkan = 2^n.
# Contoh: jika n = 2 maka total kombinasi ada 2^2 = 4.

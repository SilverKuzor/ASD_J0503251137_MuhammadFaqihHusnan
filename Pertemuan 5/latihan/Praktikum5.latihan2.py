#==================================================
# Nama  : Muhammad Faqih Husnan
# NIM   : J0403251137
# Kelas : B2 TPL
#==================================================
# Latihan 2: Tracing Rekursi

def countdown(n):

    # Kondisi berhenti rekursi
    if n == 0:
        print("Selesai")
        return

    # Eksekusi sebelum memanggil fungsi rekursif
    print("Masuk:", n)

    # Pemanggilan fungsi secara rekursif
    countdown(n - 1)

    # Eksekusi setelah fungsi rekursif selesai
    print("Keluar:", n)


countdown(3)


# ==========================
# Penjelasan:
# Pesan "Masuk" ditampilkan di awal sebelum rekursi dimulai.
# Pesan "Keluar" ditampilkan di akhir setelah rekursi selesai.
# Mekanisme stack (LIFO) menyebabkan urutan "Keluar" terbalik.

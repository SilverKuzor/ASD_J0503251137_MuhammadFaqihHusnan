#==================================================
# Nama  : Muhammad Faqih Husnan
# NIM   : J0403251137
# Kelas : B2 TPL
#==================================================
#materi 4: Backtracking kombinasi biner (n)
#==================================================
def biner(n, hasil=""):
    # Fungsi rekursif untuk membangkitkan seluruh kombinasi biner
    # n     : jumlah digit biner yang diinginkan
    # hasil : variabel penampung sementara untuk kombinasi yang sedang dikonstruksi

    # Base case - kondisi pemerhentian rekursi
    # Ketika panjang hasil sudah mencapai n,
    # berarti satu kombinasi lengkap → tampilkan hasilnya
    if len(hasil) == n:
        print(hasil)
        return

    # Recursive case - langkah rekursif
    # Pilih dan eksplorasi cabang pertama:
    # Tambahkan digit '0' dan rekursi ke level berikutnya
    biner(n, hasil + "0")

    # Pilih dan eksplorasi cabang kedua:
    # Tambahkan digit '1' dan rekursi ke level berikutnya
    biner(n, hasil + "1")

# Eksekusi fungsi
# Menghasilkan semua kombinasi biner dengan jumlah digit 3
biner(3)
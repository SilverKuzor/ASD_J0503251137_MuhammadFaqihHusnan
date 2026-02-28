#==================================================
# Nama  : Muhammad Faqih Husnan
# NIM   : J0403251137
# Kelas : B2 TPL
#==================================================
# Materi 5: Backtracking untuk menghasilkan deret biner dengan batasan jumlah digit '1'
#==================================================
def biner_batas(n, batas, hasil="", jumlah_1=0):
    # Fungsi rekursif yang menghasilkan semua kombinasi bilangan biner
    # dengan panjang n digit, di mana jumlah digit '1' tidak boleh melebihi nilai batas
    #
    # n        : panjang deret biner yang ingin dibuat
    # batas    : nilai maksimum untuk jumlah digit '1'
    # hasil    : deret biner yang sedang dibangun
    # jumlah_1 : penghitung jumlah digit '1' dalam deret saat ini

    # Pruning: Berhenti jika jumlah '1' sudah melampaui batas yang ditentukan
    if jumlah_1 > batas:
        return

    # Kasus dasar: Ketika deret biner sudah mencapai panjang n, cetak hasilnya
    if len(hasil) == n:
        print(hasil)
        return

    # Kasus rekursif: Coba menambahkan digit '0' atau '1'

    # Menambahkan digit '0' ke deret (jumlah_1 tidak berubah)
    biner_batas(n, batas, hasil + "0", jumlah_1)

    # Menambahkan digit '1' ke deret (jumlah_1 bertambah 1)
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)


# Eksekusi fungsi
# Buat deret biner dengan 4 digit, dengan jumlah '1' maksimal sebanyak 2
biner_batas(4, 2)

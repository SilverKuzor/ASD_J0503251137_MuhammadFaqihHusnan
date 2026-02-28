#==================================================
# Nama  : Muhammad Faqih Husnan
# NIM   : J0403251137
# Kelas : B2 TPL
#==================================================
# Studi Kasus: Generator PIN (Backtracking)

def buat_pin(panjang, hasil=""):

    # Kondisi berhenti:
    # Ketika jumlah digit PIN sudah mencapai target
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return

    # Coba semua kemungkinan digit yang tersedia
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)


buat_pin(3)


# ==========================
# Keterangan:
# Setiap posisi digit memiliki 3 pilihan (0, 1, 2).
# Jumlah total kombinasi = 3^3 = 27 PIN.
#
# Jika ingin menghindari digit yang sama muncul 2x:
#
# for angka in ["0", "1", "2"]:
#     if angka not in hasil:
#         buat_pin(panjang, hasil + angka)
#
# Hasilnya akan berkurang menjadi 3! = 6 kombinasi saja.
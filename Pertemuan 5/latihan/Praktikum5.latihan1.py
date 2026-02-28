#==================================================
# Nama  : Muhammad Faqih Husnan
# NIM   : J0403251137
# Kelas : B2 TPL
#==================================================
# Latihan 1: Rekursi Pangkat
# Tujuan: Memahami base case dan recursive case

def pangkat(a, n):
    # Kondisi berhenti: ketika n mencapai 0, kembalikan 1
    if n == 0:
        return 1

    # Pemanggilan rekursif: kalikan a dengan hasil pangkat(a, n-1)
    return a * pangkat(a, n - 1)


# Contoh pemanggilan
print("Hasil:", pangkat(2, 4))  # Output: 16


# ==========================
# Penjelasan:
# Kondisi berhenti (base case) mencegah rekursi tak terbatas.
# Fungsi terus memanggil dirinya dengan nilai n yang berkurang 1.
# Setiap pemanggilan menunggu hasil dari pemanggilan sebelumnya
# sebelum menyelesaikan komputasi.

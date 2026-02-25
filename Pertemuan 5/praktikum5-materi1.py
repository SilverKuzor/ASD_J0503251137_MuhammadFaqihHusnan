#================================================
# Algoritma dan Struktur data Pertemuan 4
# Nama : Muhammad Faqih Husnan
# NIM : J0403251137
# Kelas : TPL B2
#================================================

#================================================
# Materi Rekursif : Faktorial
# recursive case => 3! = 3 x 2 x 1 
# base case => 0  berhenti
#================================================

def faktorial(n):
    #base case nya
    if n == 0:
        return 1
    #recursive case
    return n*faktorial(n-1) #n-1*n-2*n-3..............n-n
print("=========== program faktorial============")
print("Hasil Faktorial : ", faktorial(5))
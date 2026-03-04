#==================================================
# Nama  : Muhammad Faqih Husnan
# NIM   : J0403251137
# Kelas : B2 TPL
#==================================================
# Latihan 1: Memahami Kode Program (Insertion Sort)

def insertion_sort(data):
 for i in range(1, len(data)):
     key = data[i]
    j = i - 1

 while j >= 0 and data[j] > key:
    data[j + 1] = data[j]
    j -= 1

 data[j + 1] = key

 return data

''''
Soal:
1. Mengapa perulangan dimulai dari indeks 1?
2. Apa fungsi variabel key?
3. Mengapa digunakan while, bukan for?
4. Operasi apa yang terjadi di dalam while?

'''
''''
Jawab :
1. Karena karenangan index ke 0 dianggakap sudah ter sorted(terurut) dengan sendirinya
2. Key berfungsi sebagai penyimpanan sementara agar nilai sebelumnya tak hilang
3. Karena for tidak cocok untuk kasus ini, dikarenakan pergeseran yang akan dilakukan tidak diketahui berapa kali, while
    lah yang cocok untuk kasus ini
4. Terjadinya pergeseran tumpuan, elemen lebih besar dari key ditukar dengan key (j-1)
'''

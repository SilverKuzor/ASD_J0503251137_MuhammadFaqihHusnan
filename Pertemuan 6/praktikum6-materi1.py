#================================================
# Algoritma dan Struktur data Pertemuan 6
# Nama : Muhammad Faqih Husnan
# NIM : J0403251137
# Kelas : TPL B2
#================================================

#================================================
# INSERTION SORT (ASCENDING)
#================================================

def insertion_sort(data):
    #Loop mulai dari data ke 2 (index array ke 1)
    for i in range(1, len(data)):
        
        key = data[i] #simpan nilai yang disisipkan
        j = i-1 #index  untuk elemen terakhir di bagian kiri
        
        #menggeser key ke j-1
        while j>=0 and data[j] > key:
            data[j+1] = data[j]
            j-=1
        #sisipkan key ke posisi yang benar
        data[j+1] = key
    return data

angka = [7,8,5,2,4,6]
print("Hasil Sorting : ", insertion_sort(angka))
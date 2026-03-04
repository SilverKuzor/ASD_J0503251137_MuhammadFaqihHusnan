#================================================
# Algoritma dan Struktur data Pertemuan 6
# Nama : Muhammad Faqih Husnan
# NIM : J0403251137
# Kelas : TPL B2
#================================================

#================================================
# INSERTION SORT DENGAN TRACING
#================================================

def insertion_sort(data):
    
    #melihat data awal
    print("Data Awal: ", data)
    print("="*50)
    #Loop mulai dari dara ke 2 (index array ke 1)
    
    for i in range(1, len(data)):
        
        
        
        
        key = data[i] #simpan nilai yang disisipkan
        j = i-1 #index  untuk elemen terakhir di bagian kiri
        print("Iterasi Ke-", i)
        print("Nilai key = ", key)
        print("Bagian kiri (terurut): ", data[:i])
        print("Bagian kanan (tak terurut): ", data[i:])
        
        #menggeser key ke j-1
        while j>=0 and data[j] > key:
            data[j+1] = data[j]
            j-=1
            print
        #sisipkan key ke posisi yang benar
        data[j+1] = key
        
        print("Setelah disisipkan :", data)
        print("-"*50)
        
    return data

angka = [7,8,5,2,4,6]
print("Hasil Sorting : ", insertion_sort(angka))
#==================================================
# Nama  : Muhammad Faqih Husnan
# NIM   : J0403251137
# Kelas : B2 TPL
#==================================================

# Latihan 3 : Tracing Insertion Sort

'''''
Buat program dengan menggunakan algoritma insertion sort
Tracing dengan data = [5, 2, 4, 6, 1, 3]
'''''

def insertion_sort(data):
    
    print("Data Awal: ", data)
    print("="*50)
    
    for i in range(1, len(data)):
        
        
        
        
        key = data[i]
        j = i-1
        print("Iterasi Ke-", i)
        print("Nilai key = ", key)
        print("Bagian kiri (terurut): ", data[:i])
        print("Bagian kanan (tak terurut): ", data[i:])
        
        while j>=0 and data[j] > key:
            data[j+1] = data[j]
            j-=1
            
        data[j+1] = key
        
        print("Setelah disisipkan :", data)
        print("-"*50)
        
    return data



angka = [5, 2, 4, 6, 1, 3]
print("Hasil Sorting : ", insertion_sort(angka))

'''
soal:
1. Tuliskan isi list setelah iterasi i = 1.
2. Tuliskan isi list setelah iterasi i = 3.
3. Berapa kali pergeseran terjadi pada iterasi i = 4?
=========================================================
jawab:
1. Iterasi Ke- 1
Nilai key =  2
Bagian kiri (terurut):  [5]
Bagian kanan (tak terurut):  [2, 4, 6, 1, 3]
Setelah disisipkan : [2, 5, 4, 6, 1, 3]

2. Iterasi Ke- 3
Nilai key =  6
Bagian kiri (terurut):  [2, 4, 5]
Bagian kanan (tak terurut):  [6, 1, 3]
Setelah disisipkan : [2, 4, 5, 6, 1, 3]

3. ada 4 pergeseran di i = 4
'''
#================================================
# Algoritma dan Struktur data Pertemuan 5
# Nama : Muhammad Faqih Husnan
# NIM : J0403251137
# Kelas : TPL B2
#================================================

#================================================
# Materi Rekursif : Menjumlahkan Elemen List
#================================================

def jumlah_list(data, index=0):
    if index == len(data):
        return 0
    
    return data[index] + jumlah_list(data, index+1)

print("=========Program Jumlah Data============")
print(jumlah_list([2,4,5,6,8]))
#=======================================================
# Praktikum 1 - Konsep ADT dan File Handling
#Latihan Dasar 1A : Membaca seluruh isi file
#=======================================================

# Membuka file dalam mode read
# Membuka file dalam satu string
with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    isi_file = file.read() # Membaca seluruh isi file dalam 1 string
print(isi_file) # Menampilkan isi file

print("==== hasil read ====")
print("Tipe Data: ", type(isi_file)) #mengecek type data
print("Jumlah Karakter : ", len(isi_file)) # Menghitung jumlah karakter
print("Jumlah baris : ", isi_file.count('\n') + 1)  
# Menambahkan 1 untuk baris terakhir jika tidak diakhiri newline

#membuka file per baris
print("==== Membaca file per baris ====")
jumlah_baris = 0
with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() # Menghilangkan karakter newline dan spasi di awal/akhir
        print("Baris ke-", jumlah_baris)
        print("isinya : ", baris)

#=======================================================
# Praktikum 1 - Konsep ADT dan File Handling
#Latihan Dasar 2 : Parsing baris menjadi kolom data
#=======================================================

with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(',') # Memisahkan kolom berdasarkan koma
        print("NIM : ", nim, "| Nama : ", nama, "| Nilai : ", nilai)
        
        
#=======================================================
# Praktikum 1 - Konsep ADT dan File Handling
#Latihan Dasar 3 : Membaca File dan Menyimpan ke dalam List
#=======================================================

data_list = []  # Inisialisasi list kosong untuk menyimpan data mahasiswa

with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(',') 
        #simpan sebagai list " [nim,nama,nilai]"
        data_list.append([nim,nama,int(nilai)])
        
print("==== Data Mahasiswa dalam List ====")
print(data_list)

print("==== Jumlah record dalam List ====")
print("Jumlah Record : ", len(data_list))

print("==== Menampilkan Data Record Tertentu ====")
print("Contoh record pertama :", data_list[0])  # Menampilkan record pertama'


#=======================================================
# Praktikum 1 - Konsep ADT dan File Handling
#Latihan Dasar 4 : Membaca file dan menyimpan ke dalam Dictionary
#=======================================================

data_dict = {}  # Inisialisasi dictionary kosong untuk menyimpan data mahasiswa
with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(',') 
        #simpan sebagai dictionary dengan key NIM
        data_dict[nim] = {  #key
            'nama': nama,   #value
            'nilai': int(nilai)
        }
print("==== Data Mahasiswa dalam Dictionary ====")
print(data_dict)

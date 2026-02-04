#=========================================
# Praktikum 2 - Konsep ADT dan File Handling
# Latihan 1 Load data
#=========================================

nama_file = "data_mahasiswa.txt"

#membuat fungsi membaca data mahasiswa dari file
def baca_data_mahasiswa(nama_file):

    data_dict = {}  # Inisialisasi dictionary kosong untuk menyimpan data mahasiswa
    with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
        for baris in file:
            baris = baris.strip()
            
            parts = baris.split(',')
            if len(parts) != 3:
                continue  # Lewati baris yang tidak sesuai format
            nim, nama, nilai_str = parts
            nilai_int = int(nilai_str)
            data_dict[nim] = {  #key
                'nama': nama,   #value
                'nilai': nilai_int
            }
    return data_dict

#memanggil fungsi baca_data_mahasiswa
buka_data = baca_data_mahasiswa(nama_file)
print("Jumlah data terbaca : ", len(buka_data))


#=========================================
# Praktikum 2 - Konsep ADT dan File Handling
# Latihan 2 membuat fungsi menampilkan data
#=========================================

def tampilkan_data_mahasiswa(data_dict):
    if len(data_dict) == 0:
        print("Data mahasiswa kosong.")
        return
    #membuat header tabel
    print("\n======== Daftar Mahasiswa ========")
    print(f"{'NIM': <10} {'Nama': <12} {'Nilai': >5}")
    print("-" * 34) #garis header sebanyak 32 karakter
    
    '''
    untuk tampilan rapi gunakan formating string dengan f-string
        {NIM: <10}  #artinya:
        tampilkan nim <= 10 rata kiri dengan lebar 10 karakter
        {Nama: <12} #artinya:
        tampilkan nama <= 12 rata kiri dengan lebar 12 karakter
        {Nilai: >5} #artinya:
        tampilkan nilai >= 5 rata kanan dengan lebar 5 karakter
        
    '''
    
    
    for nim in sorted(data_dict):
        nama = data_dict[nim]['nama']
        nilai = data_dict[nim]['nilai']
        print(f"{nim: <10} | {nama: <12} | {nilai: >5}")
        


#=========================================
# Praktikum 2 - Konsep ADT dan File Handling
# Latihan 3 membuat fungsi mencari data
#========================================   

def cari_data_mahasiswa(data_dict) :
    #Mencari data mahasiswa
    nim_cari = input("\nMasukkan NIM yang dicari : ").strip()
    if nim_cari in data_dict:
        nama = data_dict[nim_cari]['nama']
        nilai = data_dict[nim_cari]['nilai']
        print("\n=========== Data mahasiswa ditemukan ===========")
        print(f"NIM : {nim_cari}")
        print(f"Nama : {nama}")
        print(f"Nilai : {nilai}")
    else:
        print("Data dengan NIM tersebut tidak ditemukan.")
        

#=========================================
# Praktikum 2 - Konsep ADT dan File Handling
# Latihan 4 membuat fungsi update nilai
#=========================================
def update_nilai_mahasiswa(data_dict):
    
    #cari nim mahasiswa yang akan diupdate nilainya
    nim = input("\nMasukkan NIM mahasiswa yang nilainya akan diupdate : ").strip()
    
    #cek apakah nim ada dalam data_dict
    if nim not in data_dict:
        print("Data dengan NIM tersebut tidak ditemukan, update dibatalkan.")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru : (0-100)").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan.")
        return
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 hingga 100. Update dibatalkan.")
        return
    nilai_lama = data_dict[nim]['nilai']
    #memasukkan nilai baru ke dalam dictionary
    data_dict[nim]['nilai'] = nilai_baru
    
    print(f"Nilai mahasiswa dengan NIM {nim} berhasil diupdate dari {nilai_lama} menjadi {nilai_baru}.")
    


#=========================================
# Praktikum 2 - Konsep ADT dan File Handling
# Latihan 5 membuat fungsi simpan data ke file
#=========================================

def simpan_data(nama_file,data_dict):
    with open(nama_file,'w',encoding='utf-8') as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]['nama']
            nila = data_dict[nim]['nilai']
            file.write(f"{nim},{nama},{nila}\n")




#=========================================
# Praktikum 2 - Konsep ADT dan File Handling
# Latihan 6 membuat menu program
#=========================================

def main():
    
    #menjalankan fungsi 1 load data
    buka_data = baca_data_mahasiswa(nama_file)
    
    while True:
        print("\n===== Menu Program Manajemen Data Mahasiswa =====")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Mahasiswa")
        print("3. Update Nilai Mahasiswa")
        print("4. Simpan Data ke File")
        print("5. Keluar Program")
        
        pilihan = input("Masukkan pilihan (1-5) : ").strip()
        
        if pilihan == '1':
            tampilkan_data_mahasiswa(buka_data)
        elif pilihan == '2':
            cari_data_mahasiswa(buka_data)
        elif pilihan == '3':
            update_nilai_mahasiswa(buka_data)
        elif pilihan == '4':
            simpan_data(nama_file,buka_data)
            print(f"Data berhasil disimpan ke file {nama_file}.")
        elif pilihan == '5':
            print("Keluar dari program. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.") 
            
            
main()
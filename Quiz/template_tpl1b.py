# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Muhammad Faqih Husnan
# NIM     : J0403251137
# Kelas   : TPL B2
# ==============================================================================

# 1. FILE HANDLING & DICTIONARY (Sub-CPMK 1) [cite: 31]

# fungsi untuk membaca file buku.txt dan menyimpannya ke dalam Dictionary
# format file: kode_buku,judul,harga
def muat_data_buku(nama_file):
    # membuat dictionary kosong untuk menyimpan data buku
    database_buku = {}
    
    # membuka file dengan mode read dan encoding utf-8
    with open(nama_file, "r", encoding="utf-8") as file:
        # membaca setiap baris dalam file
        for baris in file:
            # menghapus spasi/enter di awal dan akhir baris
            baris = baris.strip()
            
            # skip/melewati baris kosong
            if not baris:
                continue
            
            # memecah baris menjadi 3 bagian: kode_buku, judul, harga
            kode_buku, judul, harga = baris.split(",")
            
            # menghapus tanda kutip dari judul jika ada
            judul = judul.strip('"')
            
            # menyimpan ke dictionary dengan kode_buku sebagai key
            database_buku[kode_buku] = {
                "judul": judul,
                "harga": harga,
            }
    
    # mengembalikan dictionary yang sudah terisi
    return database_buku

# 2. LINKED LIST - MANAJEMEN PROMOSI (Sub-CPMK 2) [cite: 32]
class NodePromosi:
    def __init__(self, judul):
        self.judul = judul
        self.next = None

class LinkedListPromosi:
    def __init__(self):
         self.head = None

    def tambah_buku_promosi(self, judul):
        """Menambahkan buku ke daftar promosi (Linked List)"""
        new_node = NodePromosi(judul)
        # Men set head jika tidak ada
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
            
        temp.next = new_node

    def tampilkan_promosi(self):
        """Menampilkan semua buku dalam daftar promosi"""
        # Jika Promosi nya Kosong
        if not self.head:
            print(">>> Daftar promosi kosong!")
            return
        
        print("\n--- Daftar Buku Promosi ---")
        temp = self.head
        no = 1
        #Pengulangan sesuai Promosi Buku yang di inputkan
        while temp:
            print(f"{no}. {temp.judul}")
            temp = temp.next
            no += 1 

# 3. QUEUE - ANTIREAN KASIR (Sub-CPMK 3) [cite: 33]
class NodeQueue:
    def __init__(self, nama_pelanggan):
        self.nama = nama_pelanggan
        self.next = None

class AntreanKasir:
    def __init__(self):
        self.antrean = None
        self.tail = None
        
    def is_empty(self):
        return self.antrean is None

    def tambah_antrean(self, nama_pelanggan):
        """Menambah antrean (Enqueue) - FIFO"""
        nodeBaru = NodeQueue(nama_pelanggan)
        
        if self.is_empty():
            self.antrean = nodeBaru
            self.tail = nodeBaru
            print(f">>> {nama_pelanggan} masuk ke antrean")
            return
        
        self.tail.next = nodeBaru
        self.tail = nodeBaru
        print(f">>> {nama_pelanggan} masuk ke antrean")
    
    def layani_pelanggan(self):
        """Menghapus antrean (Dequeue) - FIFO"""
        #Jika queue kosong, head dan tail menunjuk ke node yg sama
        if self.is_empty():
            print(">>> Antrean kosong!")
            return None
        
        #Jika queue tidak kosong:
        #Tail lama menunjuk ke node baru      
        data_terhapus = self.antrean.nama
        #Tail pindah ke node baru
        self.antrean = self.antrean.next
        
            
        print(f">>> Melayani: {data_terhapus}")

        return data_terhapus

    def tampilkan_antrean(self):
        """Menampilkan semua antrean"""
        if self.is_empty():
            print(">>> Antrean kosong!")
            return
        
        print("\n--- Antrean Kasir ---")
        temp = self.antrean
        no = 1
        while temp:
            print(f"{no}. {temp.nama}")
            temp = temp.next
            no += 1

# 4. SORTING - LAPORAN TRANSAKSI (Sub-CPMK 4) [cite: 34]
def urutkan_transaksi(list_harga):
    """
    Mengurutkan list harga secara manual menggunakan Insertion Sort.
    """
    # Membuat salinan agar tidak mengubah list asli
    hasil = list_harga.copy()
    
    for i in range(1, len(hasil)):
        key = hasil[i]
        j = i - 1
        
        # Menggeser elemen yang lebih besar dari key ke kanan
        while j >= 0 and hasil[j] > key:
            hasil[j + 1] = hasil[j]
            j -= 1
        
        hasil[j + 1] = key
    
    return hasil

# ==============================================================================
# MAIN PROGRAM - MENU ANTARMUKA
# ==============================================================================
def main():
    # Inisialisasi Data
    file_db = "Quiz/buku.txt"
    data_buku = muat_data_buku(file_db)
    list_promosi = LinkedListPromosi()
    antrean_toko = AntreanKasir()
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]

    while True:
        print("\n" + "="*50)
        print("--- SISTEM MANAJEMEN TOKO BUKU ---")
        print("="*50)
        print("1. Lihat Katalog Buku (Dictionary/File)")
        print("2. Kelola Daftar Promosi (Linked List)")
        print("3. Kelola Antrean Kasir (Queue)")
        print("4. Lihat Laporan Penjualan Terurut (Sorting)")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            print("\n--- Katalog Buku ---")
            for kode, info in data_buku.items():
                print(f"{kode}: {info['judul']} - Rp {info['harga']}")
        
        elif pilihan == '2':
            print("\n--- Menu Promosi ---")
            print("1. Lihat Data Promosi Buku")
            print("2. Tambah Data Promosi Buku")
            pil = input("Pilih (1/2) : ")
            if pil == '2':
                judul_baru = input("Masukkan judul buku untuk promosi: ")
                list_promosi.tambah_buku_promosi(judul_baru)
                print(">>> Buku ditambahkan ke daftar promosi")
            elif pil == '1':
                list_promosi.tampilkan_promosi()
            else:
                print("Pilihan tidak valid!")

        elif pilihan == '3':
            print("\n--- Menu Antrean Kasir ---")
            print("1. Tambah Antrean")
            print("2. Layani Pelanggan")
            print("3. Lihat Antrean")
            pil = input("Pilih (1/2/3) : ")
            
            if pil == '1':
                nama = input("Nama Pelanggan: ")
                antrean_toko.tambah_antrean(nama)
            elif pil == '2':
                antrean_toko.layani_pelanggan()
            elif pil == '3':
                antrean_toko.tampilkan_antrean()
            else:
                print("Pilihan tidak valid!")

        elif pilihan == '4':
            print("\n--- Laporan Transaksi ---")
            print(f"Harga Sebelum Urut: {riwayat_transaksi}")
            hasil_sort = urutkan_transaksi(riwayat_transaksi)
            print(f"Harga Sesudah Urut: {hasil_sort}")

        elif pilihan == '5':
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()


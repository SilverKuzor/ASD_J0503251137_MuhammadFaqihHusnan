#================================================
# Algoritma dan Struktur data Pertemuan 4
# Nama : Muhammad Faqih Husnan
# NIM : J0403251137
# Kelas : TPL B2
#================================================

#================================================
# Studi Kasus : Sistem Antrian Layanan Akademik
# Implementasi Queue =>
# Enqueue : memindahkan pointer tail (menambah data baru dari belakang)
# dequeue : memindahkan pointer head (menghapus data dari belakang)
# Front/Head -> A -> B -> C ->Rear/Tail
#================================================)

#1) mendefinisikan node (unit dasar linked list)
class Node:
    def __init__(self,nim,nama):
        self.nim = nim       # menyimpan NIM mahasiswa
        self.nama = nama     # menyimpan Nama mahasiswa
        self.next  = None    # Pointer ke node berikutnya
    
#2) Mendefinisikan queue, terdiri dari head dan tail
class queueAkademik:
    def __init__(self):
        self.head = None
        self.tail = None
    def is_empty(self):
        #ketika queue kosong maka front = rear = none
        return self.head is None
    #Menambahkan Data baru ke bagian belakang (rear)
    def enqueue(self,nim,nama):
        #Jika queue tidak kosong maka data baru diletakkan setelah rear kemudian dijadikan sebagai rear
        nodeBaru = Node(nim,nama)
        #Jika data baru  masuk dari queue yang kosong , maka data baru = front = rear
        if self.is_empty():
            self.head = nodeBaru
            self.tail = nodeBaru
            return
        self.tail.next = nodeBaru
        self.tail = nodeBaru
        
    #Menghapus data paling depan (Memberikan Layanan Akademik)
    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong, tidak ada mahasiswa yang dilayani")
            return None
        #Lihat data bagian Front, simpan di variabel data yang akan dihapus (dilayani)
        node_dilayani = self.head
        # Geser pointer front ke next front
        self.head = self.head.next
        return node_dilayani
    def tampilkan(self):
        
        
        print("Daftar antrian mahasiswa (Head -> tail) ")
        current = self.head
        no = 1
        while current is not None:
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next
            no += 1
            
    #Program Utama
def main():
        #instantiasi queue
    q = queueAkademik()
        
    while True:
        print("========== Sistem Antrian Akademik ==========")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat antrian")
        print("3. Keluar")
            
        pilihan = input("Pilih menu (1-4) : ").strip()
            
        if pilihan == "1":
            nim = input("Masukkan NIM : ").strip()
            nama = input("Masukkan Nama : ").strip()
                
            q.enqueue(nim, nama)
            print("Mahasiswa Berhasil Dilayani ")
    
            
        elif pilihan == "2":
            dilayani = q.dequeue()
            print(f"Mahasiswa Dilayani : {dilayani.nim} - {dilayani.nama}")
    
        elif pilihan == "3":
            q.tampilkan()
            
        elif pilihan == "4":
            print("Program Selesai. Terima kasih")
        else:
            print("Pilihan tidak valid. Silahkan coba lagi (1-4)")

if __name__ == "__main__":
    main()
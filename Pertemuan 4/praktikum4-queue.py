#================================================
# Algoritma dan Struktur data Pertemuan 4
# Nama : Muhammad Faqih Husnan
# NIM : J0403251137
# Kelas : TPL B2
#================================================

#================================================
#Implementasi Dasar : Queue berbasis Linked List
#================================================

#Membuat Class Node (Merupakan unit dasar dari linked list)
class Node:
    def __init__(self,data):
        self.data = data #Menyimpan Nilai / Data
        self.next = None #pointer ke note berikutnya

#Queue dengan 2 pointer : Head/Front and Tail/Rear
class QueueLL:
    def __init__(self):
        self.head = None # Node paling depan
        self.tail = None # Node paling belkang
        
    def is_empty(self):
        #Queue kosong jika 
        return self.head is None
        
    def enqueue(self,data):
        # Menambah data dibelakang(tail)
        nodeBaru = Node(data)
        
        #Jika queue kosong, head dan tail menunjuk ke node yg sama
        if self.is_empty():
            self.head = nodeBaru
            self.tail = nodeBaru
            return
        #Jika queue tidak kosong:
        #Tail lama menunjuk ke node baru        
        self.tail.next = nodeBaru
        #Tail pindah ke node baru
        self.tail = nodeBaru
        
    def dequeue(self):
        #menghapus data dari depan
        
        
        #1)Lihat data yang paling depan
        data_terhapus = self.head.data
        
        #2)Geser front ke node berikutnya
        self.head = self.head.next
        
        #3)Jika setelah geser head terjadi none, maka queue  kosong
        #rear juga harus jadi none
        if self.head is None:
            self.tail = None
            
        return data_terhapus
            
        
    def tampilkan(self):
        #Menampilkan isi queue dari head ke tail
        current = self.head
        print("Head", end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("Tail")

#Instantiasi objek class QueueLL        
q = QueueLL()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

q.tampilkan()

q.dequeue()
q.tampilkan()

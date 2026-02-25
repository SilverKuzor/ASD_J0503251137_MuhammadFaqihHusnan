#================================================
# Algoritma dan Struktur data Pertemuan 4
# Nama : Muhammad Faqih Husnan
# NIM : J0403251137
# Kelas : TPL B2
#================================================

#================================================
#Implementasi Dasar : Node pada Linked List
#================================================

#Membuat Class Node (Merupakan unit dasar dari linked list)
class Node:
    def __init__(self,data):
        self.data = data #Menyimpan Nilai / Data
        self.next = None #pointer ke note berikutnya
    
# 1) Membuat node satu per satu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2) Manghubungkan Node : A -> B -> C -> None
nodeA.next = nodeB
nodeB.next = nodeC

# 3) Menentukan node pertama (head)
head = nodeA

# 4) Traversal : Menelusuri dari head sampai none
current = head
while current is not None :
    print(current.data)
    current = current.next
    
#=====================================================
# Implementasi Dasar : Linked List + Insert Data Awal
#=====================================================

class LinkedList: #class implementasi stack
    def __init__(self):
        self.head = None #Awalnya Kosong
        
    def insert_awal(self, data) : #push dalam stack
        # 1) Buat node baru
        nodeBaru = Node(data) #panggil class node
        
        # 2) node naru menunjuk ke head lama
        nodeBaru.next = self.head
        
        # 3) head pindah ke node baru
        self.head = nodeBaru
        
    def hapus_awal(self): #pop dalam stack
        data_terhapus = self.head.data #peek dalam stack
        # Menggeser head ke node berikutnya
        self.head = self.head.next
        print("Node yang dihapus adalah ", data_terhapus)
        
    def tampilkan(self):
        current = self.head
        while current is not None :
            print(current.data)
            current = current.next
            
print("========= List Baru ==========")
ll = LinkedList() #instantiasi objek ke class linked list
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()
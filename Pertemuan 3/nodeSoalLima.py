#================================================
# Algoritma dan Struktur data Pertemuan 3
# Nama : Muhammad Faqih Husnan
# NIM : J0403251137
# Kelas : TPL B2
#================================================
#=======================
#      SOAL 5
#=======================

# Single Linkedlist node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # Tambahkan pointer tail
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head: # Jika linked list kosong
            self.head = new_node
            self.tail = new_node # Tail juga menunjuk ke node pertama
        else:
            self.tail.next = new_node # Sambungkan tail ke node baru
            self.tail = new_node # Update tail ke node baru
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")



    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next  # Simpan next
            current.next = prev       # Balik arah pointer
            prev = current            # Geser prev
            current = next_node       # Geser current

        self.head = prev  # Head baru adalah node terakhir

    
ll = LinkedList()

data_input = input("Masukkan element ke Singular linked list, pisahkan dengan spasi : ")
data = data_input.strip().split()
for i in data:
    ll.insert_at_end(int(i))
print("Sebelum di reverse :\n")
ll.display()
ll.reverse()
print("Setelah di reverse :\n")
ll.display()



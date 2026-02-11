#================================================
# Algoritma dan Struktur data Pertemuan 3
# Nama : Muhammad Faqih Husnan
# NIM : J0403251137
# Kelas : TPL B2
#================================================
#=======================
#      SOAL 1
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

    def delete_node(self, key):
        temp = self.head

        # Jika node yang mau dihapus adalah head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None

        # Cari node dengan key
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # Jika key tidak ditemukan
        if temp is None:
            return

        # Hapus node
        prev.next = temp.next
        temp = None
    
ll = LinkedList()

data_input = input("Masukkan element ke singular linked list, pisahkan dengan spasi : ")
data = data_input.strip().split()
for i in data:
    ll.insert_at_end(int(i))
ll.display()

hapus = input("Masukkan Data yang ingin dihapus : ")
ll.delete_node(int(hapus))
ll.display()


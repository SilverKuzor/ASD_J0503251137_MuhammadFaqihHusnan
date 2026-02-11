#================================================
# Algoritma dan Struktur data Pertemuan 3
# Nama : Muhammad Faqih Husnan
# NIM : J0403251137
# Kelas : TPL B2
#================================================
#=======================
#      SOAL 3
#=======================

# Doubly Linkedlist node


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Menyimpan node terakhir untuk traversing mundur

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display_forward(self):
        print("\nTraversing forward:")
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("null")

    def display_backward(self):
        print("\nTraversing backward:")
        temp = self.tail

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev

        print("null")

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                print("Data ", key, " Ditemukan")
                return True
            temp = temp.next
        print("Data ", key, " Tidak Ditemukan")
        return False 


# Contoh Penggunaan
cdll = DoublyLinkedList()

#Input nodes
data_input = input("Masukkan ke doubly linked list pisahkan dengan spasi : ")
data = data_input.strip().split()
for i in data:
    cdll.insert_at_end(int(i))
    


cdll.display_forward()
cdll.display_backward()

#Input nodes yang ingin dicari
cari = input("Masukkan angka yang mau di cari : ")
print(cdll.search(int(cari)))


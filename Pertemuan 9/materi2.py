#================================================
# Algoritma dan Struktur data Pertemuan 9
# Nama : Muhammad Faqih Husnan
# NIM : J0403251137
# Kelas : TPL B2
#================================================

#================================================
# Latian 2 : Binary tree sederana
#================================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan
        
    #membuat root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")
root.right.right = Node("F")

#menampilkan isi node
print("Data pada root ", root.data)
print("Data child kiri root ", root.left.data)
print("Data child kanan root ", root.right.data)
print("Data child kiri dari b ", root.left.left.data)
print("Data child kanan dari b ", root.left.right.data)
print("Data child kanan dari C ", root.right.right.data)

# Penjelasan :
# Kelas Node masih sama seperti sebelumnya, digunakan untuk mendefinisikan struktur dasar node pada tree.

# Root dibuat dengan nilai "A" sebagai awal dari tree.

# Selanjutnya ditambahkan child level 1, yaitu "B" sebagai anak kiri dan "C" sebagai anak kanan dari root.

# Kemudian dibuat child level 2, di mana node "B" memiliki anak "D" di kiri dan "E" di kanan, sedangkan node "C" memiliki anak "F" di kiri dan "G" di kanan.

# Terakhir, program menampilkan data pada root beserta child kiri dan kanan.
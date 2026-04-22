#================================================
# Algoritma dan Struktur data Pertemuan 9
# Nama : Muhammad Faqih Husnan
# NIM : J0403251137
# Kelas : TPL B2
#================================================

#================================================
# Latian 3 : Membuat Traversal Preorder
#================================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan
        
#Funsi preorder : left ==> root ==> right2
def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)
        
#membuat tree
    #membuat root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")
root.right.right = Node("F")

#Menjalankan traversal preorder
print("Hasil traversal preorder: ")
preorder(root)

#Penjelasan : 
# Kelas Node masih sama seperti sebelumnya, digunakan untuk membentuk struktur dasar node pada tree.

# Fungsi preorder digunakan untuk melakukan traversal dengan urutan mengunjungi node saat ini terlebih dahulu, lalu ke child kiri, dan terakhir ke child kanan secara rekursif.

# Tree dibuat dengan root "A", kemudian memiliki child "B" dan "C", serta node "B" memiliki anak "D" di kiri dan "E" di kanan.

# Selanjutnya fungsi preorder dijalankan dengan root sebagai parameter, sehingga menghasilkan urutan kunjungan A B D E C sesuai aturan preorder.
       
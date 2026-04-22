#================================================
# Algoritma dan Struktur data Pertemuan 9
# Nama : Muhammad Faqih Husnan
# NIM : J0403251137
# Kelas : TPL B2
#================================================

#================================================
# Latian 3 : Membuat Traversal Inorder
#================================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan
        
#Funsi inorder : Root ==> left ==> right
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)
        
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

print("Hasil traversal inorder: ")
inorder(root)

#penjelasan:
# Kelas Node masih sama seperti sebelumnya, digunakan untuk membentuk struktur dasar node pada tree.

# Fungsi inorder digunakan untuk traversal dengan urutan mengunjungi child kiri terlebih dahulu, lalu node saat ini, dan terakhir child kanan secara rekursif.

# Tree dibuat dengan root "A", memiliki child "B" dan "C", serta node "B" memiliki anak "D" di kiri dan "E" di kanan.

# Kemudian fungsi inorder dijalankan dengan root sebagai parameter, sehingga menghasilkan urutan D B E A C sesuai aturan inorder.
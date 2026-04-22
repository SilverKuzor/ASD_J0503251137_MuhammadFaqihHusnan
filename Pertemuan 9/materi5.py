#================================================
# Algoritma dan Struktur data Pertemuan 9
# Nama : Muhammad Faqih Husnan
# NIM : J0403251137
# Kelas : TPL B2
#================================================

#================================================
# Latian 5 : Membuat Traversal Postorder
#================================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan
        
#Funsi postorder : left ==> right ==> root
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")
        
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
print("Hasil traversal postorder: ")
postorder(root)

#Penjelasan : 
# Kelas Node masih sama seperti sebelumnya, digunakan untuk membentuk struktur dasar node pada tree.

# Fungsi postorder digunakan untuk traversal dengan urutan mengunjungi child kiri terlebih dahulu, lalu child kanan, dan terakhir node saat ini secara rekursif.

# Tree dibuat dengan root "A", memiliki child "B" dan "C", serta node "B" memiliki anak "D" di kiri dan "E" di kanan.

# Kemudian fungsi postorder dijalankan dengan root sebagai parameter, sehingga menghasilkan urutan D E B C A sesuai aturan postorder.

        
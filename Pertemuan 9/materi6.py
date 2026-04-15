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
        
        
#Funsi preorder : left ==> root ==> right
def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)
        
#membuat tree struktur oranisasi
    #membuat root
root = Node("Direktur")

#membuat child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

#membuat child level 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")

root.right.right = Node("Staff 3")

#Menjalankan traversal preorder
print("Hasil traversal postorder: ")

print("Struktur oranisasi (Preorder)")
preorder(root)

#Penjelasan : 
        
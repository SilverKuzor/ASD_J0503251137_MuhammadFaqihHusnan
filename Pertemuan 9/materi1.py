#================================================
# Algoritma dan Struktur data Pertemuan 9
# Nama : Muhammad Faqih Husnan
# NIM : J0403251137
# Kelas : TPL B2
#================================================

#================================================
# Latian 1 : membuat node
#================================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self,data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan
        
    #membuat root
root = Node("A")
    
    #menampilkan isi node
print("Data pada root ", root.data)
print("Data child kiri root ", root.left)
print("Data child kanan root ", root.right)

#Pembahasan : ................
# Kelas Node digunakan untuk membentuk struktur dasar node pada tree, yang memiliki data serta referensi ke anak kiri dan kanan.

# Konstruktor init berfungsi untuk menginisialisasi node saat dibuat, dengan mengisi nilai data dan mengatur left serta right menjadi None.

# Root dibuat dengan nilai "A" sebagai titik awal dari tree.

# Program kemudian menampilkan data pada root beserta anak kiri dan kanan. Karena belum ada penambahan node, keduanya masih bernilai None.
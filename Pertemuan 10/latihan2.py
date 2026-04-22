#================================================
# Algoritma dan Struktur data Pertemuan 10
# Nama : Muhammad Faqih Husnan
# NIM : J0403251137
# Kelas : TPL B2
#================================================

# ===============================================
# Latihan 4: Membuat BST yang Tidak Seimbang
# ===============================================

# Membuat struktur node BST
class Node:
    def __init__(self, data):
        self.data = data      # menyimpan nilai node
        self.left = None      # child kiri
        self.right = None     # child kanan

# Fungsi untuk memasukkan data ke BST
def insert(root, data):
    if root is None:
        return Node(data)     # buat node baru jika kosong
    
    if data < root.data:
        root.left = insert(root.left, data)   # masuk ke kiri
    elif data > root.data:
        root.right = insert(root.right, data) # masuk ke kanan
    
    return root               # kembalikan root

# Traversal preorder (root-kiri-kanan)
def preorder(root):
    if root is not None:
        print(root.data, end=" ")  # cetak data
        preorder(root.left)        # ke kiri
        preorder(root.right)       # ke kanan

# Menampilkan struktur tree (hierarki)
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print(" " * level + f"{posisi}: {root.data}") # tampilkan node
        tampil_struktur(root.left, level + 1, "L")    # child kiri
        tampil_struktur(root.right, level + 1, "R")   # child kanan

# Program utama
if __name__ == '__main__':
    root = None               # root awal kosong
    
    data_list = [10, 20, 30] # data berurutan naik
    
    for data in data_list:
        root = insert(root, data) # masukkan ke BST
        
    print("Preorder BST:")
    preorder(root)            # tampilkan preorder
    
    print("\n\nStruktur BST:")
    tampil_struktur(root)     # tampilkan struktur

#================================================
# Kesimpulan
#================================================
# 1. BST menjadi tidak seimbang (condong ke kanan)
# 2. Terjadi karena input data urut (ascending)
# 3. Struktur tree mirip linked list (linear)
# 4. Performa search jadi lebih lambat (O(n))
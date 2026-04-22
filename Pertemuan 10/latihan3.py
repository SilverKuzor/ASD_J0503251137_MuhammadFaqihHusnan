#================================================
# Algoritma dan Struktur data Pertemuan 10
# Nama : Muhammad Faqih Husnan
# NIM : J0403251137
# Kelas : TPL B2
#================================================

# ===============================================
# Latihan 5: Rotasi Kiri pada BST Tidak Seimbang
# ===============================================

# Membuat struktur node BST
class Node:
    def __init__(self, data):
        self.data = data      # menyimpan nilai node
        self.left = None      # child kiri
        self.right = None     # child kanan

# Traversal preorder (root-kiri-kanan)
def preorder(root):
    if root is not None:
        print(root.data, end=" ")  # cetak data
        preorder(root.left)        # ke kiri
        preorder(root.right)       # ke kanan

# Menampilkan struktur tree (hierarki)
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print("   " * level + f"{posisi}: {root.data}") # tampilkan node
        tampil_struktur(root.left, level + 1, "L")      # child kiri
        tampil_struktur(root.right, level + 1, "R")     # child kanan

# Rotasi kiri untuk menyeimbangkan tree
def rotate_left(x):
    y = x.right          # ambil child kanan sebagai root baru
    T2 = y.left          # simpan subtree kiri dari y
    
    y.left = x           # x jadi child kiri y
    x.right = T2         # T2 jadi child kanan x
    
    return y             # kembalikan root baru

# Program utama
root = Node(10)          # root awal
root.right = Node(20)    # child kanan
root.right.right = Node(30) # child kanan berikutnya (tree condong kanan)

print("Preorder sebelum rotasi kiri:")
preorder(root)           # tampilkan sebelum rotasi

print("\n\nStruktur sebelum rotasi kiri:")
tampil_struktur(root)    # struktur awal

root = rotate_left(root) # lakukan rotasi kiri

print("\nPreorder sesudah rotasi kiri:")
preorder(root)           # tampilkan setelah rotasi

print("\n\nStruktur sesudah rotasi kiri:")
tampil_struktur(root)    # struktur akhir

#================================================
# Kesimpulan
#================================================
# 1. Rotasi kiri memperbaiki tree yang condong ke kanan
# 2. Child kanan naik menjadi root baru
# 3. Root lama turun menjadi child kiri
# 4. Tree menjadi lebih seimbang dan efisien
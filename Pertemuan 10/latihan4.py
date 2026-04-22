#================================================
# Algoritma dan Struktur data Pertemuan 10
# Nama : Muhammad Faqih Husnan
# NIM : J0403251137
# Kelas : TPL B2
#================================================

# ===============================================
# Latihan 6: Rotasi Kanan pada BST Tidak Seimbang
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
        print(" " * level + f"{posisi}: {root.data}") # tampilkan node
        tampil_struktur(root.left, level + 1, "L")    # child kiri
        tampil_struktur(root.right, level + 1, "R")   # child kanan

# Rotasi kanan untuk menyeimbangkan tree
def rotate_right(y):
    x = y.left           # ambil child kiri sebagai root baru
    T2 = x.right         # simpan subtree kanan dari x
    
    x.right = y          # y jadi child kanan x
    y.left = T2          # T2 jadi child kiri y
    
    return x             # kembalikan root baru

# Program utama
if __name__ == '__main__':
    # Membuat tree tidak seimbang (condong ke kiri)
    root = Node(30)
    root.left = Node(20)
    root.left.left = Node(10)

    print("Preorder sebelum rotasi kanan:")
    preorder(root)        # tampilkan sebelum rotasi

    print("\n\nStruktur sebelum rotasi kanan:")
    tampil_struktur(root) # struktur awal

    root = rotate_right(root) # lakukan rotasi kanan

    print("\nPreorder sesudah rotasi kanan:")
    preorder(root)        # tampilkan setelah rotasi

    print("\n\nStruktur sesudah rotasi kanan:")
    tampil_struktur(root) # struktur akhir

#================================================
# Kesimpulan
#================================================
# 1. Rotasi kanan memperbaiki tree yang condong ke kiri
# 2. Child kiri naik menjadi root baru
# 3. Root lama turun menjadi child kanan
# 4. Tree menjadi lebih seimbang dan efisien
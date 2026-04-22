#================================================
# Algoritma dan Struktur data Pertemuan 10
# Nama : Muhammad Faqih Husnan
# NIM : J0403251137
# Kelas : TPL B2
#================================================

#================================================
# Latian 1 : BST
#================================================

# Membuat struktur node untuk Binary Search Tree (BST)
class Node:
    def __init__(self,data):
        self.data = data      # menyimpan nilai node
        self.left = None      # pointer ke child kiri
        self.right = None     # pointer ke child kanan
        
# Fungsi untuk memasukkan data ke BST sesuai aturan (kiri < root < kanan)
def insert(root,data):
    if root is None:
        return Node(data)     # buat node baru jika kosong
    
    if data < root.data:
        root.left = insert(root.left,data)   # masuk ke kiri
    elif data > root.data:
        root.right = insert(root.right,data) # masuk ke kanan
        
    return root               # kembalikan root

# Mengisi BST dari list data
root = None                   # awalnya kosong
data_list = [50,30,70,20,40,50,80]  # data input

for data in data_list:
    root = insert(root,data)  # masukkan satu per satu
    
print("BST berhasil dibuat")  # konfirmasi

#================================================
# Latian 2 : Traversal Inorder
#================================================

# Menampilkan isi BST dengan urutan kiri-root-kanan (hasilnya terurut)
def inorder(root):
    if root is not None:
        inorder(root.left)    # ke kiri dulu
        print(root.data, end=" ") # tampilkan data
        inorder(root.right)   # ke kanan
        
print("Hasil inorder: ")
inorder(root)                # panggil traversal

#================================================
# Latian 3: Search di BST
#================================================

# Mencari nilai dalam BST (True jika ada, False jika tidak)
def search(root,key):
    
    if root is None:
        return False          # tidak ditemukan
    
    if root.data == key:
        return True           # ditemukan
    elif key < root.data:
        return search(root.left,key)  # cari ke kiri
    else:
        return search(root.right,key) # cari ke kanan

# Uji pencarian
key = 40                     # nilai yang dicari

if search(root,key):
    print("Data ditemukan")  # hasil jika ada
else:
    print("Data Tidak ditemukan") # hasil jika tidak ada
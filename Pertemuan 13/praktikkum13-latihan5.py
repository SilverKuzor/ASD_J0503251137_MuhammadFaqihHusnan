# ================================================================
# Nama  : Muhammad Faqih Husnan
# NIM   : J0403251137
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree
# Latihan 5 - Tugas Mandiri: Kasus Jaringan Komputer
# ================================================================

# kasus yang dipilih: jaringan komputer
# algoritma yang digunakan: Kruskal

# daftar edge dalam bentuk: (bobot, node1, node2)
edges = [
    (3, 'RouterA', 'RouterB'),
    (2, 'RouterA', 'RouterC'),
    (5, 'RouterB', 'RouterD'),
    (1, 'RouterC', 'RouterD'),
    (4, 'RouterB', 'RouterC')
]

# menyiapkan parent untuk union-find sederhana
parent = {}

# fungsi untuk mencari akar suatu node
def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

# fungsi untuk menggabungkan dua kelompok node
def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)

    if root1 != root2:
        parent[root2] = root1
        return True
    return False

# mengambil seluruh node dari daftar edge
nodes = set()
for weight, u, v in edges:
    nodes.add(u)
    nodes.add(v)

# setiap node awalnya menjadi parent bagi dirinya sendiri
for node in nodes:
    parent[node] = node

# mengurutkan edge dari bobot terkecil
edges.sort()

# list hasil MST
mst = []

# total bobot minimum
total_weight = 0

# memilih edge satu per satu selama tidak membentuk cycle
for weight, u, v in edges:
    if union(u, v):
        mst.append((u, v, weight))
        total_weight += weight

# menampilkan hasil MST
print("Minimum Spanning Tree untuk jaringan komputer:")
for edge in mst:
    print(edge)

print("Total bobot minimum =", total_weight)

# Jawaban Analisis:
# 1. Kasus yang dipilih adalah jaringan komputer.
# 2. Algoritma yang digunakan adalah Kruskal.
# 3. Edge yang dipilih dalam MST:
#    - RouterC - RouterD = 1
#    - RouterA - RouterC = 2
#    - RouterA - RouterB = 3
# 4. Total bobot MST adalah 6.
#    Perhitungannya: 1 + 2 + 3 = 6.
# 5. Edge RouterB - RouterC tidak dipilih karena setelah tiga edge utama
#    dipilih, RouterA, RouterB, RouterC, dan RouterD sudah terhubung.
#    Menambahkan edge tersebut akan membentuk cycle.
#    Edge RouterB - RouterD juga tidak dipilih karena bobotnya lebih besar
#    dan tidak diperlukan untuk menghubungkan seluruh router.

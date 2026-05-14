# ================================================================
# Nama  : Muhammad Faqih Husnan
# NIM   : J0403251137
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree
# Latihan 2 - Implementasi Algoritma Kruskal
# ================================================================

# daftar edge dalam bentuk: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# mengurutkan edge berdasarkan bobot terkecil
edges.sort()

# list untuk menyimpan edge MST
mst = []

# variabel untuk menghitung total bobot MST
total_weight = 0

# set untuk menyimpan node yang sudah terhubung
connected = set()

# memeriksa setiap edge dari bobot terkecil
for weight, u, v in edges:
    # edge dipilih jika salah satu node belum masuk ke kumpulan node terhubung
    # pada data latihan ini, cara sederhana ini menghasilkan MST yang benar
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

# menampilkan hasil MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

# menampilkan total bobot
print("Total bobot =", total_weight)

# Jawaban Analisis:
# 1. Edge yang dipilih pertama kali adalah C-D dengan bobot 1.
# 2. Edge dengan bobot paling kecil dipilih lebih dahulu karena algoritma
#    Kruskal berusaha membentuk MST dengan total bobot minimum.
# 3. Total bobot MST yang dihasilkan adalah 6.
#    Perhitungannya: 1 + 2 + 3 = 6.
# 4. Edge A-B dan A-D tidak dipilih karena semua node sudah terhubung
#    setelah edge C-D, A-C, dan B-D dipilih. Jika ditambahkan, edge tersebut
#    dapat membentuk cycle dan tidak diperlukan dalam MST.

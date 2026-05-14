# ================================================================
# Nama  : Muhammad Faqih Husnan
# NIM   : J0403251137
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree
# Latihan 3 - Implementasi Algoritma Prim
# ================================================================

# modul heapq digunakan untuk memilih edge berbobot paling kecil
import heapq

# representasi weighted graph menggunakan dictionary
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

# fungsi algoritma Prim
def prim(graph, start):
    # node awal langsung dianggap sudah dikunjungi
    visited = set([start])

    # priority queue untuk menyimpan edge yang akan dipilih
    edges = []

    # memasukkan semua edge dari node awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    # menyimpan hasil MST
    mst = []

    # menghitung total bobot MST
    total_weight = 0

    # proses berjalan selama masih ada edge yang tersedia
    while edges:
        # mengambil edge dengan bobot paling kecil
        weight, u, v = heapq.heappop(edges)

        # edge dipilih jika node tujuan belum dikunjungi
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            # memasukkan edge baru dari node yang baru dikunjungi
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

# menjalankan Prim mulai dari node A
mst, total = prim(graph, 'A')

# menampilkan hasil MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

# menampilkan total bobot
print("Total bobot =", total)

# Jawaban Analisis:
# 1. Node awal yang digunakan adalah A.
# 2. Edge yang dipilih pertama kali adalah A-C dengan bobot 2.
# 3. Prim menentukan edge berikutnya dengan memilih edge berbobot terkecil
#    yang menghubungkan node yang sudah dikunjungi dengan node yang belum dikunjungi.
#    Setelah A-C dipilih, edge berikutnya adalah C-D dengan bobot 1,
#    lalu D-B dengan bobot 3.
# 4. Total bobot MST yang dihasilkan adalah 6.
#    Perhitungannya: 2 + 1 + 3 = 6.
# 5. Perbedaan Prim dan Kruskal:
#    - Prim membangun tree mulai dari satu node awal.
#    - Kruskal memilih edge terkecil secara global dari seluruh edge yang ada.

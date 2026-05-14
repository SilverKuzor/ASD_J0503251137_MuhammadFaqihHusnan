# ================================================================
# Nama  : Muhammad Faqih Husnan
# NIM   : J0403251137
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree
# Latihan 4 - Studi Kasus Jaringan Kabel Antar Gedung
# ================================================================

# menggunakan algoritma Prim
import heapq

# weighted graph: hubungan gedung dan biaya pemasangan kabel
graph = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungA': 5, 'GedungB': 3, 'GedungC': 1}
}

# fungsi untuk mencari minimum spanning tree dengan Prim
def prim(graph, start):
    visited = set([start])
    edges = []
    mst = []
    total_cost = 0

    # memasukkan edge awal ke priority queue
    for neighbor, cost in graph[start].items():
        heapq.heappush(edges, (cost, start, neighbor))

    # memilih edge biaya terkecil yang tidak membentuk cycle
    while edges:
        cost, u, v = heapq.heappop(edges)

        if v not in visited:
            visited.add(v)
            mst.append((u, v, cost))
            total_cost += cost

            # menambahkan kemungkinan edge baru dari gedung yang baru dipilih
            for neighbor, next_cost in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (next_cost, v, neighbor))

    return mst, total_cost

# menjalankan algoritma dari GedungA
mst, total_cost = prim(graph, 'GedungA')

# menampilkan hasil jaringan kabel minimum
print("Jaringan kabel dengan biaya minimum:")
for edge in mst:
    print(edge)

print("Total biaya minimum =", total_cost)

# Jawaban Analisis:
# 1. Algoritma yang digunakan adalah Prim.
# 2. Edge yang dipilih:
#    - GedungA - GedungC = 2
#    - GedungC - GedungD = 1
#    - GedungD - GedungB = 3
# 3. Total biaya minimum adalah 6.
# 4. MST cocok digunakan pada kasus ini karena kampus ingin menghubungkan
#    seluruh gedung dengan biaya kabel serendah mungkin tanpa membuat
#    jalur berlebih atau cycle.

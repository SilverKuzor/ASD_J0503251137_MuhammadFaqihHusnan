# ================================================================
# Nama  : Muhammad Faqih Husnan
# NIM   : J0403251137
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree
# Latihan 1 - Memahami Konsep Spanning Tree
# ================================================================

# daftar edge pada graph awal
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# contoh spanning tree yang valid
# spanning tree harus menghubungkan semua node tanpa cycle
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# menampilkan semua edge pada graph awal
print("Edge pada graph:")
for edge in edges:
    print(edge)

# menampilkan edge pada spanning tree
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

# menampilkan jumlah edge graph awal dan spanning tree
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# Jawaban Analisis:
# 1. Graph awal memiliki lebih banyak edge dan masih mengandung cycle,
#    sedangkan spanning tree hanya mengambil edge yang diperlukan agar
#    semua node tetap terhubung tanpa cycle.
# 2. Spanning tree tidak boleh memiliki cycle karena cycle membuat edge
#    menjadi berlebih dan koneksi menjadi tidak efisien.
# 3. Jumlah edge spanning tree selalu lebih sedikit karena spanning tree
#    hanya membutuhkan n - 1 edge untuk menghubungkan n node.
#    Pada contoh ini terdapat 4 node, sehingga spanning tree memiliki 3 edge.

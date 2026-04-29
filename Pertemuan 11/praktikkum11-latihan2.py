#===============================================================
# Nama : Muhammad Faqih Husnan
# NIM  : J0403251137
# Kelas: B2
#===============================================================
# Latihan 2 : Studi Kasus DFS (Eksplorasi Jalur)
#===============================================================


# Representasi graph menggunakan dictionary
# Key adalah node dalam graph
# Value adalah daftar node tetangga yang terhubung langsung
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}


def dfs(graph, node, visited):
    # Fungsi untuk melakukan penelusuran graph menggunakan DFS
    # graph   : dictionary yang menyimpan struktur graph
    # node    : node yang sedang dikunjungi
    # visited : set untuk menyimpan node yang sudah dikunjungi

    # Menandai node saat ini sebagai sudah dikunjungi
    visited.add(node)

    # Menampilkan node yang sedang dikunjungi
    print(node, end=" ")

    # Memeriksa semua tetangga dari node saat ini
    for neighbor in graph[node]:
        # Jika tetangga belum pernah dikunjungi
        if neighbor not in visited:
            # DFS akan masuk ke tetangga tersebut secara rekursif
            # Proses ini membuat DFS menelusuri satu jalur sampai paling dalam
            dfs(graph, neighbor, visited)


# Membuat set kosong untuk menyimpan node yang sudah dikunjungi
visited = set()

# Menampilkan keterangan proses DFS
print("DFS dari A:")

# Menjalankan DFS mulai dari node A
dfs(graph, 'A', visited)


#===============================================================
# Jawaban Pertanyaan Analisis
#===============================================================

# 1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
# DFS masuk ke node terdalam terlebih dahulu karena DFS menggunakan prinsip
# depth-first, yaitu menelusuri satu jalur sampai tidak ada node baru yang bisa
# dikunjungi. Setelah itu, DFS kembali ke node sebelumnya untuk mencoba jalur lain.

# 2. Apa yang terjadi jika urutan neighbor diubah?
# Jika urutan neighbor diubah, maka urutan hasil DFS juga akan berubah.
# Contohnya, jika node A memiliki neighbor ['C', 'B'] bukan ['B', 'C'],
# maka DFS akan masuk ke C terlebih dahulu sebelum ke B.

# 3. Bandingkan hasil DFS dengan BFS pada graph yang sama.
# Pada graph ini, DFS menghasilkan urutan:
# A B D E C F
#
# Jika menggunakan BFS pada graph yang sama, hasilnya:
# A B C D E F
#
# Perbedaannya, DFS menelusuri jalur sampai dalam terlebih dahulu,
# sedangkan BFS menelusuri semua node yang berada pada level terdekat dahulu.

# Output:
# DFS dari A:
# A B D E C F
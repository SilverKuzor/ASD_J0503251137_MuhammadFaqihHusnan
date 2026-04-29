#===============================================================
# Nama : Muhammad Faqih Husnan
# NIM  : J0403251137
# Kelas: B2
#===============================================================
# Latihan 1 : Studi Kasus BFS (Jalur Terdekat Lokasi)
#===============================================================

# Struktur data deque digunakan untuk membuat queue/antrian
# Queue dipakai dalam BFS karena BFS bekerja dengan prinsip FIFO
# FIFO artinya data yang pertama masuk akan diproses lebih dulu
from collections import deque


# Representasi graph menggunakan dictionary
# Key pada dictionary adalah node/lokasi
# Value berupa list yang berisi tetangga dari node tersebut
graph = {
    'Rumah': ['Sekolah', 'Toko'],
    'Sekolah': ['Perpustakaan'],
    'Toko': ['Pasar'],
    'Perpustakaan': [],
    'Pasar': []
}


def bfs(graph, start):
    # Fungsi untuk melakukan penelusuran graph menggunakan BFS
    # graph : dictionary yang menyimpan struktur graph
    # start : node awal penelusuran

    # visited digunakan untuk menyimpan node yang sudah dikunjungi
    # Tujuannya agar node tidak dikunjungi lebih dari satu kali
    visited = set()

    # queue digunakan untuk menyimpan node yang akan diproses
    # Node awal langsung dimasukkan ke dalam queue
    queue = deque([start])

    # Node awal ditandai sebagai sudah dikunjungi
    visited.add(start)

    # Perulangan berjalan selama queue masih berisi node
    while queue:
        # Mengambil node paling depan dari queue
        node = queue.popleft()

        # Menampilkan node yang sedang dikunjungi
        print(node, end=" ")

        # Memeriksa semua tetangga dari node yang sedang diproses
        for neighbor in graph[node]:
            # Jika tetangga belum pernah dikunjungi
            if neighbor not in visited:
                # Tandai tetangga sebagai sudah dikunjungi
                visited.add(neighbor)

                # Masukkan tetangga ke queue untuk diproses berikutnya
                queue.append(neighbor)


# Menampilkan keterangan proses BFS
print("BFS dari Rumah:")

# Menjalankan BFS mulai dari node Rumah
bfs(graph, 'Rumah')


#===============================================================
# Jawaban Pertanyaan Analisis
#===============================================================

# 1. Node mana yang dikunjungi pertama?
# Node yang dikunjungi pertama adalah Rumah, karena Rumah merupakan node awal
# yang dimasukkan pertama kali ke dalam queue.

# 2. Mengapa BFS cocok untuk mencari jalur terdekat?
# BFS cocok untuk mencari jalur terdekat karena BFS menelusuri graph secara melebar.
# Artinya, BFS akan mengunjungi semua tetangga terdekat terlebih dahulu sebelum
# lanjut ke level berikutnya. Karena itu, pada graph tidak berbobot, BFS dapat
# menemukan jalur dengan jumlah langkah paling sedikit.

# 3. Apa perbedaan urutan BFS jika struktur graph diubah?
# Jika struktur graph diubah, maka urutan BFS juga bisa berubah.
# Misalnya urutan tetangga dari Rumah diubah menjadi ['Toko', 'Sekolah'],
# maka Toko akan dikunjungi lebih dulu daripada Sekolah.
# Jadi, urutan BFS dipengaruhi oleh susunan neighbor dalam adjacency list.

# Output:
# BFS dari Rumah:
# Rumah Sekolah Toko Perpustakaan Pasar
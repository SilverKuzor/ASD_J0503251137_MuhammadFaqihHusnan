#===============================================================
# Nama : Muhammad Faqih Husnan
# NIM  : J0403251137
# Kelas: B2
#Pertemuan : 12
#===============================================================
# Latihan 4 : studi kasus jalur terpendek lokasi kampus
#===============================================================

import heapq  # memakai heapq untuk priority queue

graph = {  # membuat graph lokasi kampus
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},  # dari Gerbang ke Perpustakaan 6 menit dan ke Kantin 2 menit
    'Perpustakaan': {'Lab': 3},  # dari Perpustakaan ke Lab 3 menit
    'Kantin': {'Lab': 4, 'Aula': 7},  # dari Kantin ke Lab 4 menit dan ke Aula 7 menit
    'Lab': {'Aula': 1},  # dari Lab ke Aula 1 menit
    'Aula': {}  # Aula tidak memiliki jalur keluar
}  # akhir data graph


def dijkstra(graph, start):  # fungsi untuk mencari jarak terpendek dari lokasi awal
    distances = {node: float('inf') for node in graph}  # semua jarak awal dibuat tak hingga
    distances[start] = 0  # jarak dari lokasi awal ke dirinya sendiri adalah 0
    priority_queue = [(0, start)]  # priority queue menyimpan jarak dan lokasi

    while priority_queue:  # selama masih ada lokasi yang perlu diproses
        current_distance, current_node = heapq.heappop(priority_queue)  # mengambil lokasi dengan jarak terkecil

        if current_distance > distances[current_node]:  # jika jarak lama lebih besar dari jarak terbaru
            continue  # lewati agar proses lebih efisien

        for neighbor, weight in graph[current_node].items():  # mengecek semua lokasi tetangga
            distance = current_distance + weight  # menghitung jarak baru ke lokasi tetangga

            if distance < distances[neighbor]:  # jika jarak baru lebih kecil dari jarak lama
                distances[neighbor] = distance  # memperbarui jarak terpendek
                heapq.heappush(priority_queue, (distance, neighbor))  # memasukkan hasil baru ke priority queue

    return distances  # mengembalikan jarak terpendek ke semua lokasi


hasil = dijkstra(graph, 'Gerbang')  # menjalankan dijkstra dari Gerbang
print('jarak terpendek dari Gerbang Kampus:')  # menampilkan judul output
for lokasi, jarak in hasil.items():  # mengulang setiap lokasi dan jaraknya
    print(lokasi, '=', jarak, 'menit')  # menampilkan jarak terpendek tiap lokasi

# jawaban analisis:
# 1. lokasi yang paling dekat dari Gerbang adalah Kantin dengan waktu 2 menit.
# 2. waktu tempuh terpendek dari Gerbang ke Aula adalah 7 menit.
# 3. jalur langsung tidak selalu paling kecil, karena jalur lain bisa memiliki total bobot yang lebih rendah.
# 4. dijkstra cocok digunakan karena semua bobot waktu tempuh bernilai positif.

#===============================================================
# Nama : Muhammad Faqih Husnan
# NIM  : J0403251137
# Kelas: B2
#Pertemuan : 12
#===============================================================
# Latihan 5 : studi kasus jalur terpendek lokasi kampus
#===============================================================
import heapq  # memakai heapq untuk priority queue

graph = {  # membuat graph berbobot antar kota
    'Bogor': {'Jakarta': 5, 'Depok': 2},  # dari Bogor ke Jakarta bobot 5 dan ke Depok bobot 2
    'Depok': {'Jakarta': 2, 'Bandung': 6},  # dari Depok ke Jakarta bobot 2 dan ke Bandung bobot 6
    'Jakarta': {'Bandung': 7},  # dari Jakarta ke Bandung bobot 7
    'Bandung': {}  # Bandung tidak memiliki jalur keluar
}  # akhir data graph


def dijkstra(graph, start):  # fungsi untuk mencari jarak terpendek dari kota awal
    distances = {node: float('inf') for node in graph}  # semua jarak awal dibuat tak hingga
    distances[start] = 0  # jarak dari kota awal ke dirinya sendiri adalah 0
    priority_queue = [(0, start)]  # priority queue berisi pasangan jarak dan kota

    while priority_queue:  # proses berjalan selama priority queue belum kosong
        current_distance, current_node = heapq.heappop(priority_queue)  # mengambil kota dengan jarak terkecil

        if current_distance > distances[current_node]:  # jika jarak yang diambil bukan jarak terbaru
            continue  # lewati agar tidak menghitung data lama

        for neighbor, weight in graph[current_node].items():  # mengecek semua kota tujuan dari kota saat ini
            distance = current_distance + weight  # menghitung total jarak baru

            if distance < distances[neighbor]:  # jika jarak baru lebih kecil dari jarak lama
                distances[neighbor] = distance  # memperbarui jarak terpendek
                heapq.heappush(priority_queue, (distance, neighbor))  # memasukkan kota dengan jarak baru ke queue

    return distances  # mengembalikan hasil jarak terpendek


start_node = 'Bogor'  # menentukan kota awal
hasil = dijkstra(graph, start_node)  # menjalankan dijkstra dari kota Bogor

print('jarak terpendek dari Bogor:')  # menampilkan judul output
for kota, jarak in hasil.items():  # mengulang semua kota dan jaraknya
    print(start_node, '->', kota, '=', jarak)  # menampilkan jarak terpendek dari Bogor ke setiap kota

# jawaban analisis:
# 1. node awal yang digunakan adalah Bogor.
# 2. node dengan jarak paling kecil dari node awal adalah Depok dengan jarak 2.
# 3. node dengan jarak paling besar dari node awal adalah Bandung dengan jarak 8.
# 4. dijkstra bekerja dengan memilih kota yang jaraknya paling kecil lebih dulu, lalu memperbarui jarak ke kota tetangganya sampai semua jarak terpendek ditemukan.

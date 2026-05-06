#===============================================================
# Nama : Muhammad Faqih Husnan
# NIM  : J0403251137
# Kelas: B2
#Pertemuan : 12
#===============================================================
# Latihan 2 : implementasi dijkstra
#===============================================================
import heapq  # memakai heapq untuk priority queue

graph = {  # membuat graph berbobot positif
    'a': {'b': 4, 'c': 2},  # node a terhubung ke b bobot 4 dan ke c bobot 2
    'b': {'d': 5},  # node b terhubung ke d bobot 5
    'c': {'d': 1},  # node c terhubung ke d bobot 1
    'd': {}  # node d tidak memiliki tetangga
}  # akhir data graph


def dijkstra(graph, start):  # fungsi untuk mencari jarak terpendek dari node awal
    distances = {node: float('inf') for node in graph}  # semua jarak awal dibuat tak hingga
    distances[start] = 0  # jarak dari node awal ke node awal adalah 0
    priority_queue = [(0, start)]  # priority queue menyimpan pasangan jarak dan node

    while priority_queue:  # proses berjalan selama queue masih ada isinya
        current_distance, current_node = heapq.heappop(priority_queue)  # mengambil node dengan jarak terkecil

        if current_distance > distances[current_node]:  # jika jarak yang diambil sudah tidak terbaru
            continue  # lewati node tersebut

        for neighbor, weight in graph[current_node].items():  # mengecek semua tetangga dari node saat ini
            distance = current_distance + weight  # menghitung jarak baru menuju tetangga

            if distance < distances[neighbor]:  # jika jarak baru lebih kecil dari jarak lama
                distances[neighbor] = distance  # memperbarui jarak terpendek
                heapq.heappush(priority_queue, (distance, neighbor))  # memasukkan data baru ke priority queue

    return distances  # mengembalikan semua jarak terpendek


hasil = dijkstra(graph, 'a')  # menjalankan dijkstra dari node a
print('jarak terpendek dari node a:')  # menampilkan judul output
for node, distance in hasil.items():  # mengulang setiap node dan jaraknya
    print(node, '=', distance)  # menampilkan hasil jarak tiap node

# jawaban analisis:
# 1. jarak terpendek dari a ke b adalah 4.
# 2. jarak terpendek dari a ke c adalah 2.
# 3. jarak terpendek dari a ke d adalah 3.
# 4. jarak a ke d lebih kecil melalui c karena a -> c -> d memiliki bobot 2 + 1 = 3, sedangkan a -> b -> d memiliki bobot 4 + 5 = 9.
# 5. priority_queue berfungsi untuk memilih node dengan jarak sementara paling kecil lebih dulu.
# 6. dijkstra tidak cocok untuk bobot negatif karena hasil yang sudah dipilih bisa berubah lagi jika ada edge negatif.

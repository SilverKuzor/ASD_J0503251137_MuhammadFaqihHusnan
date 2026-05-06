#===============================================================
# Nama : Muhammad Faqih Husnan
# NIM  : J0403251137
# Kelas: B2
#Pertemuan : 12
#===============================================================
# Latihan 3 : implementasi bellman-ford
#===============================================================
graph = {  # membuat graph berbobot dengan bobot negatif
    'a': {'b': 5, 'c': 4},  # node a terhubung ke b bobot 5 dan ke c bobot 4
    'b': {},  # node b tidak memiliki tetangga
    'c': {'b': -2}  # node c terhubung ke b dengan bobot -2
}  # akhir data graph


def bellman_ford(graph, start):  # fungsi untuk mencari jarak terpendek dengan bellman-ford
    distances = {node: float('inf') for node in graph}  # semua jarak awal dibuat tak hingga
    distances[start] = 0  # jarak dari node awal ke dirinya sendiri adalah 0

    for _ in range(len(graph) - 1):  # relaksasi dilakukan sebanyak jumlah node dikurangi satu
        for node in graph:  # mengecek semua node dalam graph
            for neighbor, weight in graph[node].items():  # mengecek tetangga dan bobot dari node saat ini
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:  # jika jarak baru lebih kecil
                    distances[neighbor] = distances[node] + weight  # memperbarui jarak terpendek

    return distances  # mengembalikan hasil jarak terpendek


hasil = bellman_ford(graph, 'a')  # menjalankan bellman-ford dari node a
print('jarak terpendek dari node a:')  # menampilkan judul output
for node, distance in hasil.items():  # mengulang semua hasil jarak
    print(node, '=', distance)  # menampilkan jarak tiap node

# jawaban analisis:
# 1. bobot langsung dari a ke b adalah 5.
# 2. total bobot jalur a -> c -> b adalah 4 + (-2) = 2.
# 3. jalur yang lebih kecil menuju b adalah a -> c -> b.
# 4. bellman-ford dapat digunakan pada graph dengan bobot negatif karena semua edge dicek dan direlaksasi berulang.
# 5. relaksasi edge adalah proses memperbarui jarak jika ditemukan jalur yang lebih kecil.
# 6. perbedaan utamanya adalah dijkstra lebih cepat tetapi tidak cocok untuk bobot negatif, sedangkan bellman-ford bisa menangani bobot negatif tetapi lebih lambat.

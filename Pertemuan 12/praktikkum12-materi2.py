#===============================================================
# Nama : Muhammad Faqih Husnan
# NIM  : J0403251137
# Kelas: B2
# Pertemuan : 12
#===============================================================

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def bellman_ford(graph, start):
    # Inisialisasi: set semua jarak ke tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak ke titik mulai adalah 0
    distances[start] = 0
    
    # Perulangan relaksasi sebanyak (jumlah simpul - 1)
    for _ in range(len(graph) - 1):
        # Cek setiap node dalam graf
        for node in graph:
            # Cek setiap tetangga dan bobot jalurnya
            for neighbor, weight in graph[node].items():
                # Jika ditemukan jalur lebih pendek, update jaraknya
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    
    return distances

# Eksekusi fungsi
hasil = bellman_ford(graph, 'A')
print(hasil)
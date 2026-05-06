#===============================================================
# Nama : Muhammad Faqih Husnan
# NIM  : J0403251137
# Kelas: B2
#Pertemuan : 12
#===============================================================
# Latihan 1 : weighted graph dan perhitungan jalur
#===============================================================
graph = {  # membuat graph berbobot dengan dictionary bersarang
    'a': {'b': 4, 'c': 2},  # node a terhubung ke b bobot 4 dan ke c bobot 2
    'b': {'d': 5},  # node b terhubung ke d bobot 5
    'c': {'d': 1},  # node c terhubung ke d bobot 1
    'd': {}  # node d tidak memiliki tetangga
}  # akhir data graph

jalur_1 = graph['a']['b'] + graph['b']['d']  # menghitung total bobot jalur a ke b ke d
jalur_2 = graph['a']['c'] + graph['c']['d']  # menghitung total bobot jalur a ke c ke d

print('jalur 1: a -> b -> d =', jalur_1)  # menampilkan total bobot jalur pertama
print('jalur 2: a -> c -> d =', jalur_2)  # menampilkan total bobot jalur kedua

if jalur_1 < jalur_2:  # mengecek apakah jalur pertama lebih kecil
    print('jalur terpendek adalah a -> b -> d')  # menampilkan jalur pertama sebagai jalur terpendek
else:  # jika jalur pertama tidak lebih kecil
    print('jalur terpendek adalah a -> c -> d')  # menampilkan jalur kedua sebagai jalur terpendek

# jawaban analisis:
# 1. total bobot jalur a -> b -> d adalah 9.
# 2. total bobot jalur a -> c -> d adalah 3.
# 3. jalur yang dipilih sebagai jalur terpendek adalah a -> c -> d.
# 4. jalur terpendek tidak selalu ditentukan dari jumlah edge, tetapi dari total bobot yang paling kecil.

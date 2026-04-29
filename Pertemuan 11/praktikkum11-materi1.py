#===============================================================
# Nama : Muhammad Faqih Husnan
# NIM : J0403251137
# Kelas : B2
#===============================================================
# Materi 1 : Implementasi Dasar Graph
#===============================================================

#struktur data unntuk membuat antrian, kita gunakan dari library collections bawaan Python
from collections import deque


#representasi graph
graph = {
    'A':['B','C'],
    'B':['A','D'],
    'C':['A','D'],
    'D':['B','C']
}

for node in graph:
    print(node,"->",graph[node])
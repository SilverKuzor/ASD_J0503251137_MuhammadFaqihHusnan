#===============================================================
# Nama : Muhammad Faqih Husnan
# NIM : J0403251137
# Kelas : B2
#===============================================================
# Materi 2 : Implementasi DFS
#===============================================================

#struktur data unntuk membuat antrian, kita gunakan dari library collections bawaan Python
from collections import deque


#representasi graph
graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':[],
    'F':[]
    
}

def dfs(graph,node,visited):
    # fungsi untuk melakukan penelusuran graph dengan DFS
    # graph : dictionary yang menyimpan struktur dari graph
    # node : menyimpan node yang sedang dikunjungi
    # visited : menyimpan node yang sudah dikunjungi
    
    #tandai node sat ini sebagai node yang sudah dikunjungi
    visited.add(node)
    
    #tampilkan node yang sedang diunjungi
    print(node, end=" ")
    
    #periksa senua tetangga dari node saat ini
    for neighbor in graph[node]:
        
        #jika tetangga belum pernah dikunjungi
        if neighbor not in visited:
            #lakukan dfs secara rekursif ke tetangga tersebut
            dfs(graph,neighbor,visited)
            
#set visited
visited = set()

            
#menjalankan df dari A
dfs(graph,"A",visited)
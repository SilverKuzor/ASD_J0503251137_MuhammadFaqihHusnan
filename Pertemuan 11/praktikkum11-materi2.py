#===============================================================
# Nama : Muhammad Faqih Husnan
# NIM : J0403251137
# Kelas : B2
#===============================================================
# Materi 2 : Implementasi BFS
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
    'F':[],
    'G':[]
    
}

def bfs(graph,start):
    # fungsi untuk melakukan penelusuran graph dengan BFS
    # graph : dictionary yang menyimpan struktur dari graph
    # start : node awal penelusuran
    
    #Queue digunakan untuk menyimpan node yang akan diproses / dibaca
    
    queue = deque()
    
    #variabel yg digunakan untuk menyimpan node yg sudah diposes/dikunjungi
    visited = set()
    
    #masukkan node awal ke queue
    queue.append(start)
    
    #tanda node awal sebagai node uang sudah dikunjungi
    visited.add(start)
    
    
    while queue:
        #mengambil node paling depan dari queue
        node =  queue.popleft()
        
        #tampilkan node yang sedang di kunjungi
        print(node,end=" ")
        
        #periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:
            #jika tetangga belum dikunjungi maka tandai sebagai sudah dikunjungi
            if neighbor not in visited:
                # tandai sebagai sudah dikunjungi
                visited.add(neighbor)
                #masukkan tetangga ke queue untuk di prosese nanti
                queue.append(neighbor)
                
#menjalankan BFS dari node A 
bfs(graph,'A')       
    
    
    
    
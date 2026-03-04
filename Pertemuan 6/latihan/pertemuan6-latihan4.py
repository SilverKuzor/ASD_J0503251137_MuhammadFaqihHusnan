#==================================================
# Nama  : Muhammad Faqih Husnan
# NIM   : J0403251137
# Kelas : B2 TPL
#==================================================

# Latihan 4 : Memahami Kode Program (Merge Sort)

def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)


'''
Soal:
1. Apa yang dimaksud dengan base case?
2. Mengapa fungsi memanggil dirinya sendiri?
3. Apa tujuan fungsi merge()?
=============================================
jawab :
1. fungsi base case adalah untuk menghentikan kode dalam fungsi rekursif, tanpa base case, kode akan terus memanggil dirinya
    dan melakukan looping tak terhingga
2. karna fungsi tersebut memiliki metode rekursif pemanggilan diri didalam diri sendiri
3. menggabungkan 2 list yang tida terurut menjadi 1 list terurut
'''



#agar tidak eror

def merge(left, right):
    result = []
    i=0
    j=0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

#================================================
# Algoritma dan Struktur data Pertemuan 6
# Nama : Muhammad Faqih Husnan
# NIM : J0403251137
# Kelas : TPL B2
#================================================

#================================================
# Merge Sort with tracing
#================================================


def merge_sort(data,depth=0):
    indent = " " * depth #inden berdasarkan level rekursif
    print(f"{indent}merge_sort({data})")
    
    if len(data) <= 1:
        return data

#Divide membagi data menjadi 2 bagian
    mid = len(data) //2
    left = data[:mid] #slicing bagian kiri
    right = data[mid:] #slciing bagian kanan
    
    print(f"{indent}divide -> left = {left} | right = {right}")
    
    #8 ===> left 4  right 4
    #left 4 ==> mengsort ==>
    #  left 2 ==> mengsort
    
    #Recursive Call
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    merged = merge(left_sorted,right_sorted)
    print(f"{indent}merge -> {left_sorted} + {right_sorted} = {merged}")
    
    
    return merged

def merge(left, right):
    result = []
    i=0
    j=0
    
    #membandingkan elemen kiri dan kanan
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    #menambahkan sisa elemen jika ada
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


angka = [13,7,28,5,19,36,4]
print("Hasil Sorting Merge Sort: ",merge_sort(angka))
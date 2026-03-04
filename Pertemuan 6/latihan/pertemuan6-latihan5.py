#==================================================
# Nama  : Muhammad Faqih Husnan
# NIM   : J0403251137
# Kelas : B2 TPL
#==================================================

# Latihan 5 : Melengkapi fungsi merge

# def merge(left, right):
#  result = []
#  i = 0
#  j = 0

#  while i < len(left) and j < len(right):
#     if __________________________:
#         result.append(left[i])
#         i += 1
#     else:
#         result.append(right[j])
#         j += 1

#  result.extend(left[i:])
#  result.extend(right[j:])

#  return result

'''
Soal:
1. Lengkapi kondisi agar menjadi ascending.
2. Jelaskan fungsi result.extend().
===========================================================

'''

def merge(left, right):
 result = []
 i = 0
 j = 0

 while i < len(left) and j < len(right):
    if left[i] <= right[j]: #melengkapi
        result.append(left[i])
        i += 1
    else:
        result.append(right[j])
        j += 1

 result.extend(left[i:])
 result.extend(right[j:])

 return result

'''
Jawab soal 2 :
menambahkan kelompok elemen yang telah di sorting ke dalam result
'''

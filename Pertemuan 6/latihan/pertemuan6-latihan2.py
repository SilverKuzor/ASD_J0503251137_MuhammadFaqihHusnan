#==================================================
# Nama  : Muhammad Faqih Husnan
# NIM   : J0403251137
# Kelas : B2 TPL
#==================================================

# Latihan 2 : Melengkapi Potongan Kode


#Soal :
# def insertion_sort(data):
#  for i in range(1, len(data)):
#     key = data[i]
#     j = i - 1

#  while j >= 0 and ______________________:
#     data[j + 1] = data[j]
#     j -= 1

#  ______________________

#  return data
#=================================================
#Soal 1 : Lengkapi agar kondisi menjadi sorting ascending
#=================================================
def insertion_sort(data):
 for i in range(1, len(data)):
    key = data[i]
    j = i - 1

 while j >= 0 and data[j] > key: #melengkapi
    data[j + 1] = data[j]
    j -= 1

 data[j+1] = key #melengkapi

 return data

#=================================================
#Soal 2 : Ubah agar menjadi descending.
#=================================================
def insertion_sort_descending(data):
 for i in range(1, len(data)):
    key = data[i]
    j = i - 1
    
                #mengubah data[j] > key menjadi data[j] < key
 while j >= 0 and data[j] < key:
    data[j + 1] = data[j]
    j -= 1

 data[j+1] = key

 return data


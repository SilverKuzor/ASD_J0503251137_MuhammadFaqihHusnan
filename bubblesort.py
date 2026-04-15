#Tugas Bubble Sort
def bubble_sort(daftar_angka):
    n = len(daftar_angka)
    print("Data sebelumnya : ", daftar_angka)
    for i in range(n):
        sudah_rapi = True
        
        for j in range(0, n-i-1):
            print(f"Mengecek indeks ke-{j}")
            if daftar_angka[j] > daftar_angka[j+1]:
                print(f"Menukar indeks ke-{j} dengan indeks ke-{j+1}")
                daftar_angka[j],daftar_angka[j+1] = daftar_angka[j+1],daftar_angka[j]
                sudah_rapi = False
        print("Ronde saat ini : ", daftar_angka)
        if sudah_rapi:
            break
    print("Hasil sorting = ", daftar_angka)
        
data_dummy = [3, 1, 9, 6, 2, 8]
bubble_sort(data_dummy)
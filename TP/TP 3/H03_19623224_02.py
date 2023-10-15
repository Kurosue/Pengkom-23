# DESKRIPSI : Program mencari nilai maksimal dari array

# KAMUS
# m   : integer
# n   : integer
# arr : list of integer
#

# ALGORITMA
# INPUT
m = int(input('Masukkan banyak data: '))
n = int(input('Masukkan nilai N: '))
arr = [ int(input(f'Masukkan data ke-{i+1}: ')) for i in range(m)]

# PROSES
for i in range(m):
    for j in range(0, m - i - 1):
        if arr[j] > arr[j + 1]:
            # Menukar nilai di suatu index j dengan nilai setelahnya 
            # jika nilai di index j lebih besar
            c = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = c
# Output
print(f'Nilai terbesar ke-{n} adalah {arr[-n]}')

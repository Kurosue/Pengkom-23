# DESKRIPSI : PROGRAM MENENTUKAN BILAGAN HASIL PERPANGKATAN

# KAMUS
# N, k  = integer
# hasil = string
# 

# Algoritma
# Input
N = float(input('Masukkan bilangan N: '))
k = float(input('Masukkan nilai k: '))
# Proses
while N > 1 and k > 1:
    N /= k
if N == 1 or k == 1:
    hasil = 'merupakan'
else: # N != 1 or k != 1
    hasil = 'bukan merupakan'

# Output
print(f'{N} {hasil} perpangkatan {k}')

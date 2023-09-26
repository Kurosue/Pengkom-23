# NIM/NAMA  : 19623224/MUHAMMAD ADITYA RAHMADENI
# TANGGAL   : 25 SEPTERMBER 2023
# DESKRIPSI : PROGRAM MENENTUKAN BILAGAN YANG DIBENTUK DARI PERKALIAN BILANGAN RELATIF PRIMA BERGANTIAN

# KAMUS
# A,B,N = integer
# hasil = string
# 

# Algoritma
# Input
A = int(input('Masukkan bilangan A: '))
B = int(input('Masukkan bilangan B: '))
N = int(input('Masukkan bilangan N: '))
# Proses
while N > 1:
    if not N % (A*B):
        N /= (A*B)
    elif not N % A:
        N /= A
        if not N % A:
            break
        A, B = B, A
    elif not N % B:
        N /= B
        if not N % B:
            break
        A, B = B, A
if N == 1:
    hasil = 'dapat'
else:
    hasil = 'tidak dapat'

# Output
print(f'Bilangan {N} {hasil} dicapai')
# DESKRIPSI : PROGRAM MENENTUKAN JUMLAH KEGIATAN DI GEDUNG

# KAMUS
# n, i, a, b, j = integer
#

# ALGORITMA
# INPUT
n = int(input('Masukkan nilai N: '))
i = 0
a = 0
b = 0
while b < 3:
    i += 1
    j = int(input(f'Masukkan peserta kegiatan ke-{i}: '))
    if j >= n or a >= 5:
        b += 1
    elif j < n and a < 5:
        a += 1
print(f'Terdapat {a} kegiatan di gedung A dan {b} kegiatan di gedung B.')

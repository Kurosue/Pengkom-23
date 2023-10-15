# NIM/NAMA  : 19623224/MUHAMMAD ADTYA RAHMADENI
# TANGGAL   : 5 OKTOBER 2023
# DESKRIPSI : PROGRAM MEMBUAT BARIS BILAGAN DENGAN SIFAT UNIK

# KAMUS
# x, y, u, t, v =  integer
#

# ALGORITMA
# INPUT
x = int(input('Masukkan x: '))
y = int(input('Masukkan y: '))
u = 1
t = 1
v = y
for i in range(13):
    print(u, end =' ')
    if (u % v == 0 or t % v == 0) and u != 1:
        u -= 1
        t = v
        if u == 1:
            v += y
    elif u == 1 or t == 1:
        u += 1
        t = 1
    
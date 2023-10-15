# DESKRIPSI : PROGRAM PIRAMIDA BILANGAN

# KAMUS
# p, s, v = integer
#

# ALGORITMA
# INPUT
p = int(input('Masukkan panjang piramida: '))
s = int(input('Masukkan selisih: '))
v = 1
if p % 2 == 0:
    p -= 1
if p > 75:
    p = 75
for i in range(0, (p//2)+1):
    for j in range(i, (p//2)):
        print('X', end ='')
    for j in range(2*i+1):
        print(v % 10, end = '')
    for j in range(i, (p//2)):
        print('X', end ='')
    v += s
    print()

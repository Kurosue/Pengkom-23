# DESKRIPSI : PROGRAM MEMBENTUK SEGITIGA BILANGAN

# KAMUS
# N,n  = integer
# 

# Algoritma
# Input
N = int(input('Masukkkan nilai N: '))
n = 1
for i in range(1, N+1):
    if i > N//2:
        for j in range(i, N+1):
            print(n, end=' ')
            n += 1
    else:
        for j in range(0, i):
            print(n, end =' ')
            n += 1
    print()

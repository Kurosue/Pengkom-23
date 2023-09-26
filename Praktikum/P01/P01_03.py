# Deskripsi  :

# Kamus
# 

# Algoritma
# Input
kain = int(input('Jumlah Kain :'))
pita = int(input('Jumlah Pita :'))
# Proses
total_kain = kain - (1.2 + 1.5 + 2)
total_pita = pita - (0.8 + 1 + 1.3)
S, M, L = 0, 0, 0
if total_kain > 0 and total_pita > 0:
    S += 1
    M += 1
    L += 1
    if total_kain / 2 >= 1 and total_pita / 1.3 > 1:
        L = L + total_kain // 2
        total_kain -= (total_kain//2) * 2
        total_pita -= (total_pita // 1.3) * 1.3 
    if total_kain / 1.5 >= 1 and total_pita / 1 >= 1:
        M = M + total_kain // 1.5
        total_kain -= (total_kain// 1.5) * 1.5
        total_pita -= (total_pita // 1) *1 
    if total_kain / 1.2 >= 1 and total_pita / 0.8 >= 1:
        S = S + total_kain // 1.2
        total_kain -= (total_kain//1.2) * 1.2
        total_pita -= (total_pita // 0.8) *0.8
    print(f'Nona Deb dapat membuat {S} ukuran s, {M} ukuran M, {L} ukuran L')
else:
    print('Bahan tidak cukup untuk membuat baju.')  

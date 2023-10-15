# DESKRIPSI : Program mencari maksimal stasiun yang dapat dikunjungi

# KAMUS
# M     : Integer
# N     : Integer
# res   : Integer
# ind   : Integer
# loop  : Integer
# sum   : Integer
# hasil : List of Integer
#

# ALGORITMA
# INPUT
M = int(input('Masukkan uang yang dibawa Tuan Leo: '))
N = int(input('Masukkan jumlah stasiun: '))
hasil = [ int(input(f'Masukkan harga stasiun ke-{i+1}: ')) for i in range(N)]
res = 0

# Proses
for i in range(N):
    sum = hasil[i]
    ind = i
    loop = 1
    val = True
    while val and loop != N: 
        # Looping hingga total harga tiap stasion sama atau lebih dari uang(M)
        if ind == N-1: # Rute bersifat sirkular ( kembali lagi ke stasion awal jika mencapai stasion akhit)
            ind = 0
        else:
            ind += 1
        if sum + hasil[ind] > M:
            val = False
        else:
            loop +=1
            sum += hasil[ind]
        
    if loop > res:
        # Jika banyak stasiun yang dikunjungi dari satu stasiun lebih besar dari nilai stasiun sebelumnya
        urutan = i + 1
        res = loop
# Output
if res > 1:
    print(f'Tuan Leo dapat mengunjungi {res} stasiun dimulai dari stasiun ke-{urutan}.')
else: 
    print('Tuan Leo kekurangan uang.')

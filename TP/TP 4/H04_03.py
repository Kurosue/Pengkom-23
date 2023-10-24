# Dekripsi : Program menghitung kapal di suatu daerah

# Kamus
# M     : Integer
# N     : Integer
# Map   : Matrix[0...N-1][0...M-1] of char
# count : Integer
# row   : String
# val   : Boolean

# Fungsi
def detected(Map, x, y):
    val = True
    if x == N-1:
        # Jika nilai yang di cek berada di paling bawah
        # Maka perintah dijalankan
        while Map[x][y] != '0' and val:
            # setiap nilai di Map[i][j] yang bernilai 1
            # Maka, akan diubah menjadi 0
            Map[x][y] = '0'
            if y + 1 == M:
                # Jika nilai yang di cek berada di ujung kanan,
                # Maka, looping dihentikan
                val = False
            else:
                y += 1
    elif int(Map[x+1][y]):
        while Map[x][y] != '0' and val:
            # setiap nilai di Map[i][j] yang bernilai 1
            # Maka, akan diubah menjadi 0
            Map[x][y] = '0'
            if x + 1 == N:
                # Jika nilai yang di cek berada di paling bawah,
                # Maka, looping dihentikan
                val = False
            else:
                x += 1
    else:
        while Map[x][y] != '0' and val:
            # setiap nilai di Map[i][j] yang bernilai 1
            # Maka, akan diubah menjadi 0
            Map[x][y] = '0'
            if y + 1 == M:
                # Jika nilai yang di cek berada di ujung kanan,
                # Maka, looping dihentikan
                val = False
            else:
                y += 1

# Algoritma
# Input
N = int(input('Masukkan N: '))
M = int(input('Masukkan M: '))
print('Masukkkan Peta:')
Map = [['' for i in range(M)] for j in range(N)]
for i in range(N):
    row = input()
    for j in range(M):
        # Input row pada indeks j dimasukkan ke matriks Map[i][j]
        Map[i][j] = row[j]

# Algoritma
count = 0
for i in range(N):
    for j in range(M):
        # Cek setiap nilai di dalam matriks
        if int(Map[i][j]):
            # Jika nilai di matriks Map pada i,j
            # Maka, perintah dijalankan
            count += 1
            detected(Map, i, j)

# Output
if not count:
    # Jika count bernilai nol, maka perintah dijalankan
    print('Tidak terdapat kapal musuh pada peta')
else:
    print(f'Terdapat {count} kapal musuh pada peta')

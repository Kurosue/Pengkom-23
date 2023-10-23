# NIM/Nama  : 19623224/MUHAMMAD ADITYA RAHMADENI
# Tanggal   : 23 Oktober 2023
# Deksripsi : Program Menentukan Banyak Bakteri di-K dengan Jumlah Awal N

# Kamus
# N    : integer 
# K    : integer
# used : integer
# sum  : integer
# temp : integer

# Algoritma
# Fungsi
def hitung(N, K):
    used = 0
    sum = N
    temp = 0
    for i in range(1, K+1):
        temp = sum
        sum = (sum - used)*2 + sum
        used =  temp
    return sum

# Input
N = int(input())
K = int(input())
# Output
print(hitung(N,K))

# Deksripsi : Program Menentukan Banyak Bakteri di-K dengan Jumlah Awal N

# Kamus
# N    : integer 
# K    : integer
# used : integer
# sum  : integer
# temp : integer

# Algoritma
# Fungsi
def hitung(n, k):
    used = 0
    sum = N
    for i in range(1, K+1):
        # Mengulang sebanyak K
        # Mengkalikan bilangan yang baru dan ditambah dengan jumlah sebelumnya
        temp = sum
        sum = (sum - used)*2 + sum
        used = temp
    return sum

# Input
N = int(input('Masukkan N: '))
K = int(input('Masukkan K: '))
# Output
print(f'Terdapat {hitung(N,K)} Bakteri Pengkombacter.')

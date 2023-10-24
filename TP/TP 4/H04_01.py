# Dekripsi : Program mencari nilai maksimal dari total submatriks 2x2 dari sebuah matriks

# Kamus
# m     : Integer
# n     : Integer
# Map   : Matrix[0...N-1][0...M-1] of integer
# max   : Integer
# sum   : Intger


# Algoritma
# Input
m = int(input('Masukkan nilai m: '))
n = int(input('Masukkan nilai n: '))
print('Masukkan elemen matriks: ')
Map = [[0 for j in range(n)] for i in range(m)]
for i in range(m):
	baris = input().split()
	for j in range(n):
		Map[i][j] = int(baris[j])

# Proses
max = 0
sum = 0
for i in range(m-1):
	for j in range(n-1):
		# Cek nilai dalam matriks Map 
		if Map[i][j] % 2 or Map[i+1][j] % 2 or Map[i][j+1] % 2 or Map[i+1][j+1] % 2:
			# JIka salah satu nilai submatriks Map adalah ganjil
			# Maka, seluruh nilai dijumlahkan 
			sum = Map[i][j] + Map[i+1][j] + Map[i][j+1] + Map[i+1][j+1]
			if max < sum:
				# Jika nilai max lebih kecil dari nilai yang dijumlahkan
				# Maka, nilai max sama dengan nilai yang dijumlahkan 
				max = sum

# Output
if not max:
	print('Tidak ada submatriks 2x2 yang memenuhi syarat')
else:
	print(f'Jumlah maksimum submatriks berukuran 2x2 yang memiliki elemen ganjil adalah {max}')

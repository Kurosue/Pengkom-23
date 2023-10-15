# DESKRIPSI : Program mencari peserta yang tidak hadir

# KAMUS
# N,M   = integer
# hasil = list of integer
#

# ALGORITMA
# INPUT
N = int(input('Masukkan nilai N: '))
M = int(input('Masukkan nilai M: '))
hasil = [ int(input(f'Masukkan data ke-{i+1}: ')) for i in range(M)]

# Proses dan Output
print('Nomor perwakilan yang tidak datang:', end = ' ')
for i in range(1,N+1):
    # Membandingkan orang yang diundang dengan list kehadiran
    index = 0
    Sama = False
    while index < M:
        # Jika orang yang diundang maka nilai sama benar
        if i == hasil[index]:
            Sama = True
    # Jika nilai sama adalah salah, maka orang yang diundang tidak hadir
    if not Sama:
        print(i, end = ' ')

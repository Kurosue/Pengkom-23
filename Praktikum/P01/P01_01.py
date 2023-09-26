# Deskripsi  : Program Konversi Mata Uang ke Rupiah

# Kamus
# Peng, Kom, CPeng, CKom, RPeng, RKom = integer
# uang = string
# 

# Algoritma
# Input
Peng = int(input('Banyak uang Peng yang ditawarkan: '))
Kom = int(input('Banyak uang Kom yang ditawarkan: '))
CPeng = int(input('Konversi mata uang Peng ke rupiah: '))
CKom = int(input('Konversi mata uang Kom ke rupiah: '))
# Proses
uang = ''
RPeng = Peng * CPeng # Nilai peng ke rupiah 
RKom = Kom * CKom # Nilai kom ke rupiah

if RPeng > RKom:
    uang = 'Peng'
else: # RKom > RPeng
    uang = 'Kom'

# Output
print(f'Adik Tuan Kil memilih uang {uang}.')

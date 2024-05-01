def splitting(s:str) -> list[str]:
	# Fungsi splitting untuk mengubah string menjadi list dengan char ';' sebagai pemisahnya
    res = []
    temp = ''
    for i in s:
        if i == ';':
        	# Setiap char ';' ditemukan maka string temp akan dimasukkan ke list 
        	# lalu, string temp dikosongkan kemballi
            res += [temp]
            temp = ''
        else: # Jika i != ';'
        	# char i akan dimasukkan ke string temp
            temp += i
    # Menambahkan string temp ke dalam list res
    res += [temp]
    return res

def read_csv() -> list[list[str]]:
	# Fungsi untuk membaca isi file csv
    r = open(r'..\data\monster.csv', 'r')
    mons_matrix = [ splitting(i[:-1]) for i in r]
    # Mengubah isi file csv yang berupa string menjadi matrix menggunakan for loop untuk iterasi
    # setiap baris di file dan mengubahnya menjadi list lalu disatukan di dalam sebuah list
    return mons_matrix

def write_csv(input_mtrx:list[list[str]]):
	# Fungsi untuk menambah isi file csv
	mons_matrix = read_csv()
	# Membaca isi file csv sebagai matrix
	w = open(r'..\data\monster.csv', 'w')
	mons_matrix += input_mtrx
	# Menambahkan input list ke dalam matrix yang sudah ada
	for i in mons_matrix:
		w.write(';'.join(i) + '\n')
		# Menuliskan kembali setiap item di dalam matrix ke dalam file csv dengan mengubah list
		# menjadi string terlebih dahulu serta char ';' sebagai pembatas dan string '\n' pada akhir untuk menambah baris baru

def monster_manage(user_role:str):
	# Memvalidasi apakah bahwa pengguna adalah admin
	if user_role != 'admin':
		print('Lu bukan admin !??!?!?!?')
		return 0
	print("=========== Monster Management ============")
	print("Pilih aksi yang mau anda lakukan")
	print("1. Tampilkan Semua Monster ")
	print("2. Tambah Monster Baru ")
	choose = int(input("Pilihan Anda: "))
	mons_matrix = read_csv()

	if choose == 1:
		# Jika input 1 maka akan menampilkan isi file monster.csv
		header = ['ID', 'TYPE', 'ATTACK POWER', 'DEFENSE POWER', 'HEALTH POINT']
		print('|'.join([ f'{j: >14}' for j in header]))
		# Print header dengan char pembatas '|' dan padding 12
		idx = 1
		while idx < len(mons_matrix):
			# Iterasi untuk setiap baris didalam matrix yang berisi data monster
			print('|'.join([ f'{j: >14}' for j in mons_matrix[idx]]))
			# Print data monster dengan char pembatas '|' dan padding 12
			idx += 1
	elif choose == 2:
		# Jika Input 2, maka menambah monster baru ke dalam data matrix
		mons_type = input('Input Monster Type          : ')
		mons_atk = input("Input Monster Attack Power  : ")
		mons_def = input("Input Monster Defense Power : ")
		mons_hp = input("Input Monster Health Point  : ")
		idx = len(mons_matrix)
		write_csv([[f'{idx}', mons_type, mons_atk, mons_def, mons_hp]])
		# Menambahkan data monster baru ke dalam file monster.csv kembali
	else: # Jika input choose tidak valid ( bukan 1 atau 2 )
		print("Input tak valid wak !")

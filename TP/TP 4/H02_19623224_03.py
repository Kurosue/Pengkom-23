def detected(Map, i, j):
    if int(Map[i+1][j]):
        while Map[i][j] == '0':
            Map[i][j] == '0'
            i += 1
    else:
        while Map[i][j] == '0':
            Map[i][j] == '0'
            j += 1

N = int(input())
M = int(input())
print('Masukkkan Peta:')
Map = [ list(input()) for i in range(M)]
print(Map)
count = 0
for i in range(M-1):
    for j in range(N-1):
        if int(Map[i][j]):
            count += 1
            detected(Map, i, j)
print(count)

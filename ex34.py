n = int(input())
matriz = [[int(d) for d in input().split()]for j in range(n)]
for fim in range(n - 1, 0, -1):
    for i in range(0, fim):
        if matriz[i][1] < matriz[i+1][1]:
            matriz[i][1], matriz[i+1][1] = matriz[i+1][1], matriz[i][1]
            matriz[i][0], matriz[i+1][0] = matriz[i+1][0], matriz[i][0]

for i  in range(n):
    print(*matriz[i])
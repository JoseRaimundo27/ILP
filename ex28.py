linha, coluna = map(int, input().split())
matriz = [[int(x) for x in input().split()] for i in range(linha)]
sum = 0
for i in range(linha):
    for k in range(coluna):
        sum += matriz[i][k]
        if sum<0:
            sum = 0

print(sum)

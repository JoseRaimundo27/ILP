linha, coluna = map(int, input().split())
matriz = [[int(x) for x in input().split()] for i in range(linha)]
A = int(input())

quantidade_de_1 = 0
for i in range(linha):
    for j in range(coluna):
        if matriz[i][j] == 1:
            quantidade_de_1 +=1 

acertos = 0
for i in range(A):
    pos_linha, pos_coluna = map(int, input().split())
    if matriz[pos_linha - 1][pos_coluna - 1] == 1:
        acertos += 1
        matriz[pos_linha - 1][pos_coluna - 1] = 0

if acertos == quantidade_de_1:
    print("HASTA LA VISTA BABY")
else: 
    print("ILL BE BACK")


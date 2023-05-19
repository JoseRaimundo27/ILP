linha , coluna = map(int, input().split())

resultado = [[0]*coluna for i in range(linha)] # Criando a matriz resultado com mesmo nº de linhas e colunas q as matrizes A e B
matrizA = [[int(x) for x in input().split()] for i in range(linha) ] #Criando a matriz A
matrizB = [[int(x) for x in input().split()] for i in range(linha) ] #Criando a matriz B

for i in range(linha):
    for j in range(coluna):
        resultado[i][j] = matrizA[i][j] - matrizB[i][j]
        
for l in range(linha):
    print(*resultado[l])

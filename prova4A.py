linha = int(input())
matriz = [[int(x) for x in input().split()] for i in range(linha)]
vezes = int(input())
sum = 0
for i in range(vezes):
    linha_d, coluna_d = map(int, input().split())
    sum += matriz[linha_d][coluna_d] 
    
print(sum)
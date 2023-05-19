linha = int(input())
matriz = [[int(x) for x in input().split()] for i in range(linha)]
harry, ron = map(int, input().split())
sumHarry = 0
sumRon = 0
for i in range(linha):
    sumRon += matriz[i][ron]
    matriz[i][ron] = 0
    sumHarry += matriz[harry][i]
    matriz[harry][i] = 0
    
    

print("Harry", sumHarry)
print("Ron", sumRon)
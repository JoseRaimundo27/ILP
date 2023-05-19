n = int(input())
lista = [int(z) for z in input().split()]

for i in range(n-1, 0, -1):
    imaior = 0
    for k in range(1, i+1):
        if lista[k] > lista[imaior]:
            imaior = k
        
    lista[imaior], lista[i] = lista[i], lista[imaior]

for i in range(0,8):
    print(lista[i], end =" ")
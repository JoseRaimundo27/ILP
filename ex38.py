n = int(input())
lista = [str(n) for n in input().split()]
qntd = int(input())
lista2 = [str(k) for k in input().split()]
matriz = [[int(i) for i in input().split()] for k in range(n)]
arrayColuna = []

for element2 in lista2:
    for i in range(n):
        if element2 == lista[i]:
            arrayColuna.append(i)

ActualPlanet = 0
sum = 0
for k in range(len(lista2)):
    sum += matriz[ActualPlanet][arrayColuna[k]]
    ActualPlanet = arrayColuna[k]

print(sum)




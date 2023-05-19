n = int(input())
listaDoces = [int(k) for k in input().split()]
listaPar = []
listaImpar =[]
for i in listaDoces:
    if i%2 == 0:
        listaPar.append(i)
    else:
        listaImpar.append(i)

for i in range(len(listaImpar) - 1, 0, -1):
        for j in range(0, i):
            if listaImpar[j] > listaImpar[j+1]:
                listaImpar[j], listaImpar[j+1] = listaImpar[j+1], listaImpar[j]

for u in range(len(listaPar) - 1, 0, -1):
        for z in range(0, u):
            if listaPar[z] < listaPar[z+1]:
                listaPar[z], listaPar[z+1] = listaPar[z+1], listaPar[z]


listaFinal = listaImpar + listaPar
print(*listaFinal)
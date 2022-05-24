n= input()
lista = [int(k) for k in input().split()]

comparador = [0]* 1000001
for i in lista:
	comparador[i] = 1

for j in range(len(comparador)):
    if int(comparador[j]) == 1:
        print(j,"",end="")
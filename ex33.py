n =  int(input())
idade_h = [int(z) for z in input().split()]
idade_m = [int(z) for z in input().split()]

def ordenarCrescente(lista):
   for fim in range(n - 1, 0, -1):
        for i in range(0, fim):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]





def ordenarDecrescente(lista):
    for fim in range(n - 1, 0, -1):
        for i in range(0, fim):
            if lista[i] < lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]

ordenarDecrescente(idade_m)
ordenarCrescente(idade_h)


for i in range(n-1, -1, -1):
    print(str(idade_h[i]) +" " + str(idade_m[i]))
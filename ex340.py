n1, n2 = map(int, input().split())
L = []
for j in range(n1):
     l=[int(x) for x in input().split()]
     L+=l
L.sort()
n = int(input())
lista = [int(k) for k in input().split()]
for element in lista:
    esq = 0
    dir = len(L) - 1
    while esq < dir:
        meio = (esq+dir)//2
        if element > L[meio]:
            esq = meio + 1
        elif element == L[meio]:
            if L[meio] < L[len(L) - 1] and L[meio+1] == element:
                esq = meio + 1
            elif L[meio] < L[len(L) - 1] and L[meio + 1] != element:
                break
        else:
            dir = meio
    
    if element > L[meio]:
        print(len(L))
    elif element == L[meio]:
        print(esq + 1)
    else: 
        print(meio)


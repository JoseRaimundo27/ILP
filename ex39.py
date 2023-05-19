n1, n2 = map(int, input().split())
L = []
for j in range(n2):
    for i in input().split():
        L.append(int(i))
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
            break
        else:
            dir = meio
    
    if element > L[meio]:
        print(len(L) )
    elif element == L[meio]:
        if L[meio+1] == element:
            while L[meio+1] == element:
                meio = meio + 1
            print(meio + 1)
        else:
            print(meio + 1)
    else:
        print(meio)
         
    

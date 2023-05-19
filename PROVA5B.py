n_geral = int(input())
lista_geral = [str(k) for k in input().split()]
n_proibido = int(input())
lista_probido = [str(j) for j in input().split()]
n_feitiços = int(input())
feitiços = [str(u) for u in input().split()]

for z in feitiços:
    esq = 0
    dir = n_geral - 1
    while esq <= dir:
        meio = (esq + dir) // 2
        if lista_geral[meio] == z:
            break
        elif z < lista_geral[meio]:
            dir = meio - 1
        else:
             esq = meio + 1

    if lista_geral[meio] == z:
        print("Geral")
    else:
        print("Proibido")

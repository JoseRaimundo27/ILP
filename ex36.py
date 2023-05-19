n =  int(input())
vetor = [int(k) for k in input().split()]
vetor2 = [int(u) for u in input().split()]

for elem in vetor2:
    if elem == 0:
            break
    esq = 0 
    dir = n -1
    while esq < dir:
        meio = (dir + esq) // 2
        if  elem > vetor[meio]:
            esq = meio + 1
        else:
            dir = meio
    if vetor[esq] == elem:
        print(esq)
    if vetor[esq] != elem:
        print("Nao foi visitado ainda.")
   

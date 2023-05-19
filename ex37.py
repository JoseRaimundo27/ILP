qntd_selecionados , n =  map(int, input().split())
matriz = [[int(k) for k in input().split()] for j in range(n)]
for fim in range(n - 1, 0, -1):
    for i in range(0, fim):
        if matriz[i][0] < matriz[i+1][0]:
            matriz[i][0], matriz[i+1][0] = matriz[i+1][0], matriz[i][0]
            matriz[i][1], matriz[i+1][1] = matriz[i+1][1], matriz[i][1]

candidatos = int(input())
for i in range(candidatos):
    notaCandidato, idCanditado =  map(int, input().split())
    if notaCandidato > matriz[qntd_selecionados][0]:
        print("Sim")
    elif notaCandidato < matriz[qntd_selecionados][0]:
        print("Nao")
    
    elif notaCandidato == matriz[qntd_selecionados][0]:
        if idCanditado < matriz[qntd_selecionados][1]:
            print("Sim")
        else:
            print("Nao")
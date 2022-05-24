checkpoints = int(input())
soma = 0
for i in range(checkpoints):
    limite, mortes, horas_sucesso =  map(int, input().split())
    soma += (limite*mortes) + horas_sucesso

print(soma)
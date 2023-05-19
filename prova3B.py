n_cartas = int(input())
cartas = [int(k) for k in input().split()]
n_rodadas = int(input())
meus_pontos = 0
amigos_pontos = 0
for i in range(n_rodadas):
    meu_dado, amigo_dado = map(int , input().split())
    if cartas[meu_dado - 1] > cartas[amigo_dado - 1]:
        meus_pontos += 1
    elif cartas[meu_dado - 1] < cartas[amigo_dado - 1]:
        amigos_pontos += 1

if meus_pontos == amigos_pontos:
    print("Empatou")
elif meus_pontos > amigos_pontos:
    print("Venci")   
elif meus_pontos < amigos_pontos:
    print("Perdi")


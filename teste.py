N=int(input())
vc=[int(c) for c in input().split()]
R=int(input())
cont_e=0
cont_a=0
for i in range(R):
     e,a=map(int,input().split())
     cont_e+=vc[e-1]
     cont_a+=vc[a-1]
if cont_e<cont_a:
     print('Perdi')
elif cont_e>cont_a:
     print('Venci')
else:
     print('Empatou')

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


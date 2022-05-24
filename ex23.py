qntd_sapos, pedras = map(int, input().split())
for i in range(pedras):
    lista = [0]*pedras

for i in range(qntd_sapos):
    pulo = int(input())
    for k in range(0,pedras,pulo):
        lista[k] = 1

print(*lista)
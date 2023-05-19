stop = int(input())
contador = 0
for i in range(10):
    linha = []
    linha = [int(k) for k in input().split()]
    if stop in linha:
        contador = 1

if contador == 1:
    print("sim")
else:
    print("nao")
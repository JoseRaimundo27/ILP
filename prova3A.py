n = input()
partes = [int(j) for j in input().split()]
multiplicador = int(input())
resul = []

for k in partes:
    resul.append(k*multiplicador)

print(*resul)

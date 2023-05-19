linha, teleportes = map(int, input().split())
matriz = [[int(x) for x in input().split()] for i in range(linha)]
soma = 0
for j in range(teleportes):
    pos_x, pos_y = map(int, input().split())
    for k in range(pos_x,-1,-1):
        if matriz[k][pos_y] == 1:
            soma += 1
            matriz[k][pos_y] = 0
            break

print(soma)
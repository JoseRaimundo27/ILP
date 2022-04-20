n = int(input());
qtd_homem, qtd_mulher = 0 , 0
for i in range(n):
    sexo = int(input())
    if sexo == 1:
        qtd_homem += 1;
    else:
        qtd_mulher += 1;

print(qtd_homem);
print(qtd_mulher);

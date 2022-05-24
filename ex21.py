number = int(input())
lista = input().split()
esperado = ["1", "2", "3", "4" , "5" , "6" , "7"]
qual_temos =[]
for i in esperado:
    for j in lista:
        if j == i:
            qual_temos.append(i)

if qual_temos == esperado:
    print(*qual_temos)
    print("Saia Shenlong e realize o meu desejo")
else:
    print(*qual_temos)
    print("Nao encontramos todas")






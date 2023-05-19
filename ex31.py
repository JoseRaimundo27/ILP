matrizA = [[str("u") for i in range(12)] for k in range(12)] # Crio uma matriz com "u" em volta
matriz = [[str(x) for x in input().split()] for i in range(10)]
lista = ["u"]*12
for i in range(10):
    for k in range(10):
        matrizA[i+1][k+1] = matriz[i][k] # Coloco os valores da matriz dentro da matriz "u"
        
for a in range(11):
    for b in range(11):
        if matrizA[a][b] == "t":
            if (matrizA[a][b+1] == "*") or (matrizA[a][b-1] == "*") or (matrizA[a-1][b] == "*") or(matrizA[a+1][b] == "*") :
                matrizA[a][b] = "p" # Transformo em P tudo que está ao redor de "*"

            
for i in range(11): # Deleto as colunas com "u"
    del(matrizA[i][0])
    del(matrizA[i][10])


for k in range(1,11):  #Deleto as linhas com "u"
    print(*matrizA[k])


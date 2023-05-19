n, tipo, orientaçao = input().split()
n = int(n)
v = []
for i in range(n):
   nome, level = input().split()
   v.append({"nome": nome,
             "level": int(level)})

if tipo == "N" and orientaçao == "D":
    for inicio in range(1, n):
        for fim in range(n - 1, 0, -1):
            for i in range(0, fim):
                if v[i]["nome"] < v[i+1]["nome"]:
                    v[i], v[i+1] = v[i+1], v[i]

elif tipo == "N" and orientaçao == "C":
    for inicio in range(1, n):
        for fim in range(n - 1, 0, -1):
            for i in range(0, fim):
                if v[i]["nome"] > v[i+1]["nome"]:
                    v[i], v[i+1] = v[i+1], v[i]
 
elif tipo == "L" and orientaçao == "D":
    for inicio in range(1, n):
        for fim in range(n - 1, 0, -1):
            for i in range(0, fim):
                if v[i]["level"] < v[i+1]["level"]:
                    v[i], v[i+1] = v[i+1], v[i]


elif tipo == "L" and orientaçao == "C":
    for inicio in range(1, n):
        for fim in range(n - 1, 0, -1):
            for i in range(0, fim):
                if v[i]["level"] > v[i+1]["level"]:
                    v[i], v[i+1] = v[i+1], v[i]

for chave in v:
    print(chave["nome"], chave["level"])
print("Valores para tirar media:")
lista = [int(i) for i in input().split()]
sum = 0
for k in lista:
    sum += k

sum = sum/len(lista)
print(sum)
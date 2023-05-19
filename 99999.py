#Primeiras 15 linhas: 2 em 2minutos
#for i in range(1,13):
 #   print(120*i ,"%d minutos"%(i*2))

#soma = 120
#for i in range(1, 11):
 #   soma += 350
  #  print(soma)

n = int(input("numero: "))
k = int(input("valor minimo "))
while n != 0:
    print("%f quadradinhos" %((n - k)/35))
    n = int(input("numero: "))
    k = int(input("valor minimo "))
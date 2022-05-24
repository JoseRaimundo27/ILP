n = int(input())
multiplo = 0
for i in range(n+1):
    if  i%5 == 0:
        multiplo +=1
    
for k in range( 1, multiplo):
    print(k*5)



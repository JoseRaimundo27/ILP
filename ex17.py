inicio,final = map(int, input().split())
primo = 0;
for i in range(inicio, final + 1):
    multiplo = 0;
    for k in range(2, 10001):
        if i%k == 0:
            multiplo +=1;

    if multiplo == 1:
        primo += 1  

print(primo)

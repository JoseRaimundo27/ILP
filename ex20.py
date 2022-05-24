number = int(input())
list = input().split()

par = []
impar = []
for i in list:
    if int(i) % 2 == 0:
        par.append(i)
    else:
        if i not in impar:
            impar.append(i)

print(*par)
print(*impar)
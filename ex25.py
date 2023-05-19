n = int(input())
v1 =  [int(k) for k in input().split()]
v2 = [int(j) for j in input().split()]
v3 = [int(i) for i in input().split()]
resul = [];
for i in range(n):
    resul.append(v1[i] + v2[i]) 

if resul == v3:
    print("OK")
else:
    print("NOPE :(")
number = int(input())
lista = map(int, input().split())
choice = int(input())
if choice in lista:
    print(choice)
else:
    print("-1")
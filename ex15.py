enemies =  int(input());
divisivel = False
for i in range(0, 5000):
    if 2**i % enemies == 0:
        divisivel = True
    
        
if divisivel:
    print("Dattebayo")
else:
    print("Tururuuu")
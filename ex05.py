
sec = int(input());
horas = (sec//3600); #As horas serão o valor absoluto
minutos = (sec%3600)//60 # Os minutos serão o resto da divisão divido por 60
segundos = (sec%3600)%60 # Os segundos serão o resto de toda divisão
print(str(horas)+"h", str(minutos)+"m", str(segundos)+"s")

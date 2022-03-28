n = int(input());
#quantidade de doce dividido igualmente:
chapeuzinho = n//3; 
vovozinha = n//3;
loboMau = n//3;

resto = int(n%3); # calcularemos o resto e usaremos IF nas duas possibilidades possiveis

if resto == 1:
    print("Chapeuzinho Vermelho %d" %(chapeuzinho + 1));
    print("Vovozinha %d" %(vovozinha));
    print("Lobo Mau %d" %(loboMau));

elif resto == 2:
    print("Chapeuzinho Vermelho %d" %(chapeuzinho + 1));
    print("Vovozinha %d" %(vovozinha + 1));
    print("Lobo Mau %d" %(loboMau));

else:
    print("Chapeuzinho Vermelho %d" %(chapeuzinho));
    print("Vovozinha %d" %(vovozinha));
    print("Lobo Mau %d" %(loboMau));


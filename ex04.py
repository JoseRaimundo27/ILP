Q1, Q2, Q3 = input().split();
E1,E2,E3 = input().split();
caçada1 = int(Q1) - 2*int(E1) - int(E1);
caçada2 = int(Q2) - 2*int(E2) - int(E2);
caçada3 = int(Q3) - 2*int(E3) - int(E3);
qntd_ovos = caçada1 + caçada2 + caçada3;
print(int(qntd_ovos));

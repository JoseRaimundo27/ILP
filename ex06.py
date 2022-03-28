pistas, pessoasPorPista, alunos = map(int, input().split());

fator = pistas*pessoasPorPista;

if fator > alunos:
    print("S");
else:
    print("N");
    
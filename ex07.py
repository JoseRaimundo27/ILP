L1, P1 = map(int, input().split());
L2, P2 = map(int, input().split());
L3, P3 = map(int, input().split());

pontuacaoLucas = L1 + L2 + L3;
pontuacaoPedro = P1 + P2 + P3;

if pontuacaoLucas == pontuacaoPedro:
    print("Empate");
elif pontuacaoLucas > pontuacaoPedro:
    print("Lucas");
elif pontuacaoLucas < pontuacaoPedro:
    print("Pedro");
    

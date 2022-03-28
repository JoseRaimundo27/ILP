zagueiro, goleiro = input().split();
atacante, chute = input().split();

if zagueiro == atacante:
    if chute != goleiro:
        print("Driblado");
        print("...e o goleiro pega");
    else:
        print("Driblado");
        print("Gol");
else:
    print("Bloqueado");



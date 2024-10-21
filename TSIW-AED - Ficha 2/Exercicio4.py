import random

max_tentativas = 10

while True:
    numero_aleatorio = random.randint(1, 50)

    print()
    print("Jogo 'Adivinha o Número'!")
    print("Tente adivinhar o número entre 1 e 50.")

    for tentativas in range(1, max_tentativas + 1):
        palpite = int(input("Indique o seu palpite: "))

        if palpite < 1 or palpite > 50:
            print("Indique um número entre 1 e 50.")
            continue

        if palpite < numero_aleatorio:
            print("O número é Maior.")
        elif palpite > numero_aleatorio:
            print("O número é Menor.")
        else:
            print(f"Parabéns! Acertou em {tentativas} tentativas.")
            break
    else:
        print(f"Esgotou as {max_tentativas} tentativas :( O número correto era {numero_aleatorio}.")

    continuar = input("Quer jogar novamente (S/N)? ").strip().lower()
    
    match continuar:
        case 's':
            continue
        case 'n':
            print("Obrigado por jogar!")
            break
        case _:
            print("Entrada inválida! Finalizando o jogo.")
            break
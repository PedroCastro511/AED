Peso = float(input("Indique o seu peso (kg): "))
print()
print("Planetas")

lang = int(input("Indique o código do planeta: "))
match lang:
    case 1:
        pesoPlaneta = Peso * 0.37/0.98
        print(f'O seu peso de: {Peso} no planeta 1 seria de {pesoPlaneta} kg' )
    case 2:
        pesoPlaneta = Peso * 0.90/0.98
        print(f'O seu peso de: {Peso} no planeta 1 seria de {pesoPlaneta} kg' )
    case 3:
        pesoPlaneta = Peso * 0.37/0.98
        print(f'O seu peso de: {Peso} no planeta 1 seria de {pesoPlaneta} kg' )
    case 4:
        pesoPlaneta = Peso * 2.53/0.98
        print(f'O seu peso de: {Peso} no planeta 1 seria de {pesoPlaneta} kg' )
    case 5:
        pesoPlaneta = Peso * 1.06/0.98
        print(f'O seu peso de: {Peso} no planeta 1 seria de {pesoPlaneta} kg' )
    case 6:
        pesoPlaneta = Peso * 0.91/0.98
        print(f'O seu peso de: {Peso} no planeta 1 seria de {pesoPlaneta} kg' )
    case _:
        print("Código do planeta incorreto")
        exit()
	
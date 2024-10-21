numero = input("Indique um número: ")

if numero.isdigit(): 
    numero = int(numero) 
    
    if numero <= 0:
        print("Por favor, indique um número positivo.")
    else:
        soma_divisores = sum(i for i in range(1, numero) if numero % i == 0)

        if soma_divisores == numero:
            print(f"{numero} é um número perfeito.")
        else:
            print(f"{numero} não é um número perfeito.")
else:
    print("Entrada inválida! Por favor, insira um número inteiro.")

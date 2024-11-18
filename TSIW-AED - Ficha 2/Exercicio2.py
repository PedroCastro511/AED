numeroInferior = int(input("Indique o liminte inferior: "))
numeroSuperior = int(input("Indique o liminte superior: "))

if numeroInferior > numeroSuperior:
    print("O número inferior tem de ser mais baixo que o número superior")
else:
    conta = sum(numero for numero in range(numeroInferior, numeroSuperior + 1) 
    if numero % 2 == 0)
    print(f"A soma de todos os pares entre {numeroInferior} e {numeroSuperior} é: {conta}")
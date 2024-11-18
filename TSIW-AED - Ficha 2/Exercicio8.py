numero = 0

while not (1 <= numero <= 99):
    entrada = input("Digite um número entre 1 e 99: ")
    if entrada.isdigit(): 
        numero = int(entrada)
    else:
        print("Entrada inválida. Tente novamente.")

resultado = ' '.join(bin(numero)[2:])
print(f"O número: {numero} em binário fica: {resultado}")

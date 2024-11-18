import random

quantidade = int(input("Digite a quantidade de números: "))

numeros = [random.randint(1, 100) for _ in range(quantidade)]  

print("Números gerados:", numeros)

maior = None
segundo_maior = None

for numero in numeros:
    if maior is None or numero > maior:
        segundo_maior = maior  
        maior = numero  
    elif numero != maior:  
        if segundo_maior is None or numero > segundo_maior:
            segundo_maior = numero 

if segundo_maior is not None:
    print("O segundo maior valor é:", segundo_maior)
else:
    print("Não há segundo maior valor (todos os números são iguais).")

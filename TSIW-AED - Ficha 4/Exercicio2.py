import random

def generateNumbers(numero_inferior, numero_superior, quantidade):
    numeros_gerados = set()

    while len(numeros_gerados) < quantidade:
        numero = random.randint(numero_inferior, numero_superior)
        numeros_gerados.add(numero)

    return list(numeros_gerados)

euromilhoes_numeros = generateNumbers(1, 50, 5) 
euromilhoes_estrelas = generateNumbers(1, 12, 2)  

print("Números do Euromilhões:", euromilhoes_numeros)
print("Estrelas do Euromilhões:", euromilhoes_estrelas)


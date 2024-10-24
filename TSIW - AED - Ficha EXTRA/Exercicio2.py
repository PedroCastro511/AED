import re

def countWord(texto, palavra):
    matches = list(re.finditer(re.escape(palavra), texto, re.IGNORECASE))
    return len(matches), [m.start() for m in matches]

texto = input("Escreva uma frase: ")
palavra = input("Escreva a palavra que quer verificar a sua contagem: ")
ocorrencias, posicoes = countWord(texto, palavra)

print(f"A palavra '{palavra}' foi encontrada {ocorrencias} vezes nas posições: {posicoes}")


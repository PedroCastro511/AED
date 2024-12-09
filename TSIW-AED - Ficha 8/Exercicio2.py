import os
import random

FILE_PATH = ".\\files\\paises.txt"

def lerPaises():
    """Lê o ficheiro paises.txt e retorna uma lista de países."""
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            return [linha.strip() for linha in file.readlines() if linha.strip()]
    except FileNotFoundError:
        print(f"Erro: O ficheiro '{FILE_PATH}' não foi encontrado.")
        return []

def imprimePais(pais, tentativas_restantes):
    """Imprime o nome do país com caracteres ocultos ('-') e revela mais a cada tentativa."""
    visiveis = len(pais) - tentativas_restantes
    revelado = ''.join(c if i < visiveis else '-' for i, c in enumerate(pais))
    print("Ajuda:", revelado)

def adivinhaPais():
    """Função principal para o jogo Adivinha o País."""
    paises = lerPaises()
    if not paises:
        print("A lista de países está vazia. Certifique-se de que o ficheiro existe e contém países.")
        return
    
    pais_selecionado = random.choice(paises)

    print("Bem-vindo ao jogo 'Adivinha o País!'")
    print("Você tem 3 tentativas para adivinhar o nome do país sorteado.")
    print("A cada tentativa, uma letra será revelada no nome do país.\n")

    tentativas = 3
    while tentativas > 0:
        imprimePais(pais_selecionado, tentativas)
        resposta = input(f"Tentativa {4 - tentativas}: Qual é o país? ").strip()
        if resposta.lower() == pais_selecionado.lower():
            print("Parabéns! Você acertou!")
            return
        else:
            print("Resposta errada. Tente novamente.")
        tentativas -= 1

    print("\nQue pena! Você não conseguiu adivinhar.")
    print(f"O país era: {pais_selecionado}")

adivinhaPais()

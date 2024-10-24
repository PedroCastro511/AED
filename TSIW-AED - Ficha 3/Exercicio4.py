def removeSpaces(texto):
    texto_sem_espacos = ' '.join(texto.split())
    print(texto_sem_espacos)

texto = input("Escreva um texto com vários espaços: ")
removeSpaces(texto)

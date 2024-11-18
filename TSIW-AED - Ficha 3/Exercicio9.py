def printCharLine(texto, numeroCaracteres):
    for i in range(0, len(texto), numeroCaracteres):
        print(texto[i:i+numeroCaracteres])

texto = input("Escreva um texto: ")
numeroCaracteres = int(input("Escreva o número de caracteres por linha: "))
printCharLine(texto, numeroCaracteres)

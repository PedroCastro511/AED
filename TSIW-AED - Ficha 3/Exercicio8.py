def reverseWords(texto):
    palavras = texto.split()
    palavras_invertidas = palavras[::-1]
    texto_invertido = ' '.join(palavras_invertidas)
    
    return texto_invertido

texto = input("Escreva um texto: ")
print(reverseWords(texto))

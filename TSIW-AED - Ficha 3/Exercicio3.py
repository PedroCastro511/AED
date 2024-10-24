def capicua(texto):
    texto_limpo = texto.replace(" ", "").lower()
    
    return texto_limpo == texto_limpo[::-1]


texto = input("Escreva um texto: ")
if capicua(texto):
    print(f"O texto '{texto}' é uma capicua.")
else:
    print(f"O texto '{texto}' não é uma capicua.")

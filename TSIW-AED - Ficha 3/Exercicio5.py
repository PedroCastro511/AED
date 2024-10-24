def shortName(nome):
    # Dividir o nome completo em uma lista de palavras
    nome_completo = nome.split()
    
    # Pegar o primeiro nome e o último sobrenome
    primeiro_nome = nome_completo[0]
    ultimo_nome = nome_completo[-1]
    
    return f"{primeiro_nome} {ultimo_nome}"

nome = input("Escreva o seu nome completo: ")
print()
print(shortName(nome))

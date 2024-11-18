def shortName(nome):
    nome_completo = nome.split()
    
    primeiro_nome = nome_completo[0]
    ultimo_nome = nome_completo[-1]
    
    return f"{primeiro_nome} {ultimo_nome}"

nome = input("Escreva o seu nome completo: ")
print()
print(shortName(nome))
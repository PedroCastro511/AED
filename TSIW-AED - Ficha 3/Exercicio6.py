def standardName(nome):
    nome_completo = nome.split()  
    primeiro_nome = nome_completo[0]
    ultimo_sobrenome = nome_completo[-1]
    nomes_abreviados = [parte[0] + '.' for parte in nome_completo[1:-1]]
    nome_normalizado = f"{primeiro_nome} {' '.join(nomes_abreviados)} {ultimo_sobrenome}"
    return nome_normalizado

nome = input("Escreva o seu nome completo: ")
print(standardName(nome))

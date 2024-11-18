def procurarNumero(lista, pesquisa):
    posicoes = []
    for i in range(len(lista)):
        if lista[i] == pesquisa:
            posicoes.append(i)
    return posicoes

def principal():
    lista_numeros = []

    for i in range(10):
        while True:
            try:
                numero = int(input(f"Introduza o número inteiro {i + 1}: "))
                lista_numeros.append(numero)
                break
            except ValueError:
                print("Erro: Entrada inválida.")
    
    while True:
        try:
            valor_pesquisa = int(input("Introduza o valor a pesquisar na lista: "))
            break
        except ValueError:
            print("Erro: Entrada inválida.s")
    
    posicoes = procurarNumero(lista_numeros, valor_pesquisa)
    
    if posicoes:
        print(f"O valor {valor_pesquisa} foi encontrado nas posições: {posicoes}.")
    else:
        print(f"O valor {valor_pesquisa} não foi encontrado na lista.")

if __name__ == "__main__":
    principal()

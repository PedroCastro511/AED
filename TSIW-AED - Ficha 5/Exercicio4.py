def ler_matriz(linhas, colunas):
    return [[float(input(f"Introduza o valor para a posição [{i+1}][{j+1}]: ")) for j in range(colunas)] for i in range(linhas)]

def exibir_matriz(matriz):
    for linha in matriz:
        print(" ".join(f"{elemento:.2f}" for elemento in linha))

def operar_matrizes(matriz1, matriz2, operacao):
    return [[operacao(matriz1[i][j], matriz2[i][j]) for j in range(len(matriz1[0]))] for i in range(len(matriz1))]

def menu():
    print("\nMenu:")
    print("1. Somar duas matrizes")
    print("2. Subtrair duas matrizes")
    print("3. Sair")
    return input("Escolha uma opção: ")

def main():
    while True:
        opcao = menu()
        if opcao in {"1", "2"}:
            linhas = int(input("Introduza o número de linhas das matrizes: "))
            colunas = int(input("Introduza o número de colunas das matrizes: "))
            
            print("Introduza os elementos da primeira matriz:")
            matriz1 = ler_matriz(linhas, colunas)
            print("Introduza os elementos da segunda matriz:")
            matriz2 = ler_matriz(linhas, colunas)
            
            if opcao == "1":
                resultado = operar_matrizes(matriz1, matriz2, lambda x, y: x + y)
                print("Resultado da soma das matrizes:")
            else:
                resultado = operar_matrizes(matriz1, matriz2, lambda x, y: x - y)
                print("Resultado da subtração das matrizes:")
            
            exibir_matriz(resultado)
            
        elif opcao == "3":
            print("Sair do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

main()

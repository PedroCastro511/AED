import random

def inicializar_matriz():
    linhas = int(input("Digite o número de linhas da matriz: "))
    colunas = int(input("Digite o número de colunas da matriz: "))
    
    matriz = [[random.randint(10, 100) for _ in range(colunas)] for _ in range(linhas)]
    
    print("\nMatriz gerada:")
    for linha in matriz:
        print(linha)
        
    return matriz

def matriz_transposta(matriz):
    transposta = list(map(list, zip(*matriz)))
    
    print("\nMatriz Transposta:")
    for linha in transposta:
        print(linha)

def maior_valor(matriz):
    maior = max(max(linha) for linha in matriz)
    print(f"\nO maior valor da matriz é: {maior}")

def main():
    matriz = None
    
    while True:
        print("\nMenu:")
        print("1. Iniciar matriz")
        print("2. Matriz transposta")
        print("3. Maior valor")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            matriz = inicializar_matriz()
        elif opcao == '2':
            if matriz is None:
                print("Matriz não iniciada. Por favor, inicie a matriz primeiro.")
            else:
                matriz_transposta(matriz)
        elif opcao == '3':
            if matriz is None:
                print("Matriz não iniciada. Por favor, inicie a matriz primeiro.")
            else:
                maior_valor(matriz)
        elif opcao == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

main()

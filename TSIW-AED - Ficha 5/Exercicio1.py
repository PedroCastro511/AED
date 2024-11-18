def ler_matriz():
    matriz = []
    print("Introduza os elementos da matriz 3x3:")
    for i in range(3):
        linha = []
        for j in range(3):
            elemento = int(input(f"Elemento [{i+1},{j+1}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def invert(matriz):
    print("\nMatriz Original:")
    for linha in matriz:
        print(linha)

    transposta = [[matriz[j][i] for j in range(3)] for i in range(3)]
    
    print("\nMatriz Transposta:")
    for linha in transposta:
        print(linha)

matriz = ler_matriz()
invert(matriz)

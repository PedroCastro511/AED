def ordenar_sem_duplicados(lista):
    lista_sem_duplicados = list(set(lista))
    lista_sem_duplicados.sort()
    return lista_sem_duplicados

def main():
    while True:
        try:
            n = int(input("Introduza o número de elementos da lista: "))
            if n > 0:
                break
            else:
                print("Erro: O número deve ser maior que 0.")
        except ValueError:
            print("Erro: Entrada inválida.")
    
    lista_numeros = []

    for i in range(n):
        while True:
            try:
                numero = int(input(f"Introduza o elemento {i + 1}: "))
                lista_numeros.append(numero)
                break
            except ValueError:
                print("Erro: Entrada inválida.")
    
    lista_final = ordenar_sem_duplicados(lista_numeros)
    
    print(f"\nLista original: {lista_numeros}")
    print(f"Lista gerada (ordenada e sem duplicados): {lista_final}")

if __name__ == "__main__":
    main()
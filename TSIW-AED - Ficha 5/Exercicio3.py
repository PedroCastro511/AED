parque = [[False for _ in range(5)] for _ in range(3)]

def menu():
    print("\nMENU")
    print("1 - Entrada de veículo")
    print("2 - Saída de carro")
    print("3 - Estado do Parque")
    print("0 - Sair")

def entrada_veiculo():
    for fila in range(3):
        for lugar in range(5):
            if not parque[fila][lugar]:  
                parque[fila][lugar] = True  
                print(f"Veículo estacionado na Fila {fila + 1}, Lugar {lugar + 1}")
                return
    print("Parque completo") 

def saida_carro():
    try:
        fila = int(input("Indique a fila do veículo (1-3): ")) - 1
        lugar = int(input("Indique o lugar do veículo (1-5): ")) - 1
        if 0 <= fila < 3 and 0 <= lugar < 5 and parque[fila][lugar]:
            parque[fila][lugar] = False  
            print(f"Veículo removido da Fila {fila + 1}, Lugar {lugar + 1}")
        else:
            print("Posição inválida ou lugar já está vazio.")
    except ValueError:
        print("Entrada inválida! Insira números válidos para a fila e o lugar.")

def estado_parque():
    ocupados = sum(sum(fila) for fila in parque)
    livres = 15 - ocupados
    print(f"Lugares ocupados: {ocupados}")
    print(f"Lugares livres: {livres}")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            entrada_veiculo()
        elif opcao == "2":
            saida_carro()
        elif opcao == "3":
            estado_parque()
        elif opcao == "0":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()

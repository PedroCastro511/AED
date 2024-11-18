import os

def garantir_ficheiro():
    os.makedirs('files', exist_ok=True)
    if not os.path.exists('files/paises.txt'):
        open('files/paises.txt', 'w').close()


def inserir_pais():
    pais = input("Introduza o nome do país: ").strip()
    continente = input("Introduza o continente: ").strip()


    with open('files/paises.txt', 'r', encoding='utf-8') as f:
        if any(linha.startswith(pais + ";") for linha in f):
            print(f"O país {pais} já existe no ficheiro.")
            return

    with open('files/paises.txt', 'a', encoding='utf-8') as f:
        f.write(f"{pais};{continente}\n")
        print(f"O país {pais} foi adicionado ao continente {continente}.")


def consulta_paises():
    with open('files/paises.txt', 'r', encoding='utf-8') as f:
        paises = f.readlines()
        if paises:
            print("Lista de países:")
            print("\n".join(p.strip() for p in paises))
        else:
            print("Não há países registados.")


def consulta_por_continente():
    continente = input("Introduza o continente: ").strip()
    with open('files/paises.txt', 'r', encoding='utf-8') as f:
        encontrados = [pais.strip() for pais in f if pais.split(';')[1].strip() == continente]
        if encontrados:
            print(f"Países no continente {continente}:")
            print("\n".join(encontrados))
        else:
            print(f"Nenhum país encontrado para o continente {continente}.")


def consulta_numero_paises():
    continentes = {}
    with open('files/paises.txt', 'r', encoding='utf-8') as f:
        for pais in f:
            continente = pais.split(';')[1].strip()
            continentes[continente] = continentes.get(continente, 0) + 1

    print("Número de países por continente:")
    for continente, numero in continentes.items():
        print(f"{continente}: {numero} países.")

def menu():
    garantir_ficheiro()

    while True:
        print("\nMENU")
        print("1 - Inserir Países")
        print("2 - Consultar Países")
        print("3 - Consultar por Continente")
        print("4 - Consultar nº de países por continente")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            inserir_pais()
        elif opcao == '2':
            consulta_paises()
        elif opcao == '3':
            consulta_por_continente()
        elif opcao == '4':
            consulta_numero_paises()
        elif opcao == '5':
            print("A sair...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()

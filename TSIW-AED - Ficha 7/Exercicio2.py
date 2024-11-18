def consulta_dados_por_data():
    data_pesquisa = input("Introduza a data (formato: AAAA-MM-DD): ").strip()
    try:
        with open('files/temperatura.txt', 'r', encoding='utf-8') as f:
            encontrados = [linha.strip() for linha in f if linha.startswith(data_pesquisa)]
        if encontrados:
            print(f"Dados de temperatura para {data_pesquisa}:\n" + "\n".join(encontrados))
        else:
            print(f"Nenhum dado encontrado para a data {data_pesquisa}.")
    except FileNotFoundError:
        print("O ficheiro de temperatura não foi encontrado.")

def consulta_estatisticas():
    try:
        with open('files/temperatura.txt', 'r', encoding='utf-8') as f:
            temperaturas = [
                float(linha.split(';')[1]) for linha in f if linha.strip().split(';')[1].replace('.', '', 1).isdigit()
            ]
        if temperaturas:
            print(f"Temperatura mínima: {min(temperaturas):.2f}°C")
            print(f"Temperatura máxima: {max(temperaturas):.2f}°C")
            print(f"Temperatura média: {sum(temperaturas)/len(temperaturas):.2f}°C")
        else:
            print("Não há dados de temperatura para mostrar.")
    except FileNotFoundError:
        print("O ficheiro de temperatura não foi encontrado.")
    except ValueError:
        print("Erro na leitura das temperaturas.")

def menu():
    while True:
        print("\nMENU")
        print("1 - Consultar dados do ficheiro por data")
        print("2 - Consultar estatísticas")
        print("3 - Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        if opcao == '1':
            consulta_dados_por_data()
        elif opcao == '2':
            consulta_estatisticas()
        elif opcao == '3':
            print("A sair...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()

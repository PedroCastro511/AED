import os

# Caminho do ficheiro de temperatura
ficheiro = "./files/temperatura.txt"

def lerFicheiro():
    """
    Ler o ficheiro de temperaturas e devolver uma lista com o conteúdo.
    """
    try:
        with open(ficheiro, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Erro: O ficheiro '{ficheiro}' não foi encontrado.")
        return []

def consultarData():
    """
    Consulta os registos no ficheiro para uma data específica.
    """
    os.system("cls" if os.name == "nt" else "clear")
    data = input("Introduza uma data (no formato YYYY-MM-DD): ")
    
    linhas = lerFicheiro()
    if not linhas:
        input("Pressione Enter para voltar ao menu.")
        return
    
    encontrou = False
    print(f"\nRegistos para a data {data}:")
    for linha in linhas:
        campos = linha.strip().split(";")
        if len(campos) >= 2 and campos[0] == data:
            print(f"Hora: {campos[1]}, Temperatura: {campos[2]}°C")
            encontrou = True
    
    if not encontrou:
        print("Nenhum registo encontrado para a data fornecida.")
    
    input("\nPressione Enter para voltar ao menu.")

def consultarEstatistica():
    """
    Calcula a temperatura mínima, máxima e média dos dados no ficheiro.
    """
    os.system("cls" if os.name == "nt" else "clear")
    
    linhas = lerFicheiro()
    if not linhas:
        input("Pressione Enter para voltar ao menu.")
        return
    
    temperaturas = []
    for linha in linhas:
        campos = linha.strip().split(";")
        if len(campos) >= 3:
            try:
                temperaturas.append(float(campos[2]))
            except ValueError:
                print(f"Erro ao processar linha: {linha}")
    
    if temperaturas:
        temp_min = min(temperaturas)
        temp_max = max(temperaturas)
        temp_media = sum(temperaturas) / len(temperaturas)
        
        print("\nEstatísticas:")
        print(f"Temperatura Mínima: {temp_min:.2f}°C")
        print(f"Temperatura Máxima: {temp_max:.2f}°C")
        print(f"Temperatura Média: {temp_media:.2f}°C")
    else:
        print("Nenhum dado válido encontrado no ficheiro.")
    
    input("\nPressione Enter para voltar ao menu.")

def menu():
    """
    Menu principal do programa.
    """
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\nMENU")
        print("1 - Consultar por data")
        print("2 - Consultar Estatística")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            consultarData()
        elif opcao == '2':
            consultarEstatistica()
        elif opcao == '0':
            print("Sair...")
            break
        else:
            print("Opção inválida, tente novamente.")

# Chama o menu
menu()

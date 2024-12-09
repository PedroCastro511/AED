import os
import pickle

FILE_PATH = ".\\files\\dados.bin"

def escreveTexto(texto):
    """Recebe um texto e o guarda num ficheiro binário."""
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
    
    with open(FILE_PATH, "wb") as file:
        pickle.dump(texto, file)

def lerTexto():
    """Lê o conteúdo do ficheiro binário e devolve o texto."""
    try:
        with open(FILE_PATH, "rb") as file:
            texto = pickle.load(file)
        return texto
    except FileNotFoundError:
        return "Ficheiro não encontrado."

def menu():
    """Exibe um menu de opções para o utilizador."""
    while True:
        print("\nMenu:")
        print("1 - Guardar texto no ficheiro")
        print("2 - Ler texto do ficheiro")
        print("3 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            texto = input("Insira o texto a ser guardado: ")
            escreveTexto(texto)
            print("Texto guardado com sucesso!")
        elif opcao == "2":
            texto_lido = lerTexto()
            print("Texto lido do ficheiro:", texto_lido)
        elif opcao == "3":
            print("Saindo do programa. Até breve!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chamar o menu diretamente
menu()

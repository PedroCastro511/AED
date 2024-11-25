import os 

listaContinentes = ["America",  "Europa", "Asia", "Africa", "Oceania"]

def lerFicheiro():
    """
    ler ficheiro de paises e devolve uma lista com o conteudo 
    """
    filePaises = open(ficheiro, 'r', encoding = "utf-8")
    listaPaises = filePaises.readlines()
    filePaises.close()
    return listaPaises

def guardarFicheiro(pais, continente):
    filePaises = open (ficheiro, "a", encoding = "utf-8")
    linha = pais + ";" + continente + "\n"
    filePaises.write(linha)
    filePaises.close()

def inserirPaises():
    """"
    Lê paises e lê um continente e acrescenta ao ficheiro paises.txt
    """
    os.system('cls')
    pais = input("Introduza um país: ")

    continente = input("Introduza um continente: ")
    if continente not in listaContinentes:
        print("O continente não existe")
        input()
    else:
        listaPaises = lerFicheiro()
        for linha in listaPaises:
            campos = linha.split(";")
            if campos[0] == pais:
                print("O país {:s} já existe". format(pais))
                input()
                return
        guardarFicheiro(pais, continente)
#----------------------------------------------------------------#

def consultar_paises():
    listapaises = lerFicheiro()
    for linha in listapaises:
        campos = linha.split(";")
        print(campos[0],campos[1])
    input()

def consultar_por_continente():
    os.system("cls")
    continente = input("Introduza um continente: ")
    
    listapaises = lerFicheiro()
    for linha in listapaises:
        campos = linha.split(";")
        if continente == campos[1].strip("\n"):
            print(campos[0],campos[1])
    input()

#--------------------------------------------------------#

def contar_paises_por_continente():
    listaPaises = lerFicheiro()

    for continente in listaContinentes:
        numeropaises = 0 
        for linha in listaPaises:
            if linha.split(";")[1].strip("\n") == continente:
                numeropaises +=1
        print(numeropaises, continente)
    input()

#----------------------------------------------------------#
ficheiro = ".\\files\\paises.txt"
def menu():
    while True:
        os.system("cls")
        print("\nMENU")
        print("1 - Inserir Países")
        print("2 - Consulta Países")
        print("3 - Consulta por Continente")
        print("4 - Consultar nº de países por continente")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            inserirPaises()
        elif opcao == '2':
            consultar_paises()
        elif opcao == '3':
            consultar_por_continente()
        elif opcao == '4':
            contar_paises_por_continente()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

# Chama o menu
menu()
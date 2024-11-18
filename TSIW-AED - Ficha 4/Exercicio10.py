# Definição da fila de espera
maximo = 20
fila_espera = [None] * maximo
proximo_ticket = 1

def tirar_ticket():
    global proximo_ticket
    for i in range(maximo):
        if fila_espera[i] is None:
            fila_espera[i] = proximo_ticket
            print(f"Ticket {proximo_ticket} na posição {i + 1}.")
            proximo_ticket += 1
            return
    print("Fila completa.")

def atendimento():
    for i in range(maximo):
        if fila_espera[i] is not None:
            print(f"Atendendo ticket {fila_espera[i]} da posição {i + 1}.")
            fila_espera[i:] = fila_espera[i + 1:] + [None]
            return
    print("Nenhum cliente na fila.")

def estado_fila():
    ocupados = sum(t is not None for t in fila_espera)
    print(f"Lugares ocupados: {ocupados}, Lugares livres: {maximo - ocupados}.")

def menu():
    while True:
        print("\nMENU\n1 – Tirar Ticket\n2 – Atendimento\n3 – Estado da fila\n0 – Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            tirar_ticket()
        elif opcao == '2':
            atendimento()
        elif opcao == '3':
            estado_fila()
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()

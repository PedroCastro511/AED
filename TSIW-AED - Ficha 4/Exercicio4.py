def listaPositivas(nomes, pontuacoes):
    """Retorna duas listas: uma com nomes e outra com pontuações positivas (>= 10)."""
    nomes_positivos = []
    pontuacoes_positivas = []
    
    for nome, pontuacao in zip(nomes, pontuacoes):
        if pontuacao >= 10:
            nomes_positivos.append(nome)
            pontuacoes_positivas.append(pontuacao)
    
    return nomes_positivos, pontuacoes_positivas

def main():
    nomes = []
    pontuacoes = []
    
    for i in range(10):
        while True:
            nome = input(f"Digite o nome do participante {i + 1}: ")
            if nome.strip():  # Verifica se o nome não está vazio
                nomes.append(nome)
                break
            else:
                print("Erro: O nome não pode estar vazio.")

        while True:
            try:
                pontuacao = float(input(f"Digite a pontuação do participante {nome} (0 a 20): "))
                if 0 <= pontuacao <= 20:
                    pontuacoes.append(pontuacao)
                    break  # Sai do loop se a pontuação for válida
                else:
                    print("Erro: A pontuação deve estar entre 0 e 20.")
            except ValueError:
                print("Erro: Entrada inválida. Por favor, digite um número.")

    # Chama a função listaPositivas e imprime os resultados
    nomes_positivos, pontuacoes_positivas = listaPositivas(nomes, pontuacoes)
    print("\nParticipantes com pontuações positivas (>= 10):")
    for nome, pontuacao in zip(nomes_positivos, pontuacoes_positivas):
        print(f"{nome}: {pontuacao}")

if __name__ == "__main__":
    main()

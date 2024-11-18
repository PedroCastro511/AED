def listaPositivas(pontuacoes):
    return [pontuacao for pontuacao in pontuacoes if pontuacao >= 10]

def main():
    pontuacoes = []
    
    for i in range(10):
        while True:
            try:
                pontuacao = float(input(f"Introduza a pontuação do participante {i + 1} (0 a 20): "))
                if 0 <= pontuacao <= 20:
                    pontuacoes.append(pontuacao)
                    break
                else:
                    print("Erro: A pontuação deve estar entre 0 e 20.")
            except ValueError:
                print("Erro: Entrada inválida.")
    
    pontuacoes_positivas = listaPositivas(pontuacoes)
    print("Pontuações positivas (>= 10):", pontuacoes_positivas)

if __name__ == "__main__":
    main()


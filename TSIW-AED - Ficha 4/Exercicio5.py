def mes_maior_faturacao(faturacao):
    maior_faturacao = max(faturacao)
    mes = faturacao.index(maior_faturacao) + 1 
    return mes, maior_faturacao

def mes_menor_faturacao(faturacao):
    menor_faturacao = min(faturacao)
    mes = faturacao.index(menor_faturacao) + 1 
    return mes, menor_faturacao

def media_faturacao(faturacao):
    return sum(faturacao) / len(faturacao)

def main():
    faturacao = []
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", 
        "Junho", "Julho", "Agosto", "Setembro", "Outubro", 
        "Novembro", "Dezembro"
    ]

    for mes in meses:
        while True:
            try:
                valor = float(input(f"Introduza a faturação para o mês de {mes}: "))
                if valor >= 0:  
                    faturacao.append(valor)
                    break
                else:
                    print("Erro: A faturação não pode ser negativa.")
            except ValueError:
                print("Erro: Entrada inválida.")
    
    mes_max, faturacao_max = mes_maior_faturacao(faturacao)
    mes_min, faturacao_min = mes_menor_faturacao(faturacao)
    media = media_faturacao(faturacao)
    
    print(f"\nO mês com a maior faturação foi: {meses[mes_max - 1]} com {faturacao_max:.2f} unidades.")
    print(f"O mês com a menor faturação foi: {meses[mes_min - 1]} com {faturacao_min:.2f} unidades.")
    print(f"A média mensal de faturação é: {media:.2f} unidades.")

if __name__ == "__main__":
    main()

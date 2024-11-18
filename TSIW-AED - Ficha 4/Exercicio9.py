def listar_visitantes_decrescentes(visitantes):
    return sorted(visitantes, reverse=True)

def media_visitantes(visitantes):
    return sum(visitantes) / len(visitantes)

def dia_mais_proximo_media(visitantes, media):
    dias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
    mais_proximo = min(visitantes, key=lambda x: abs(x - media))
    indice = visitantes.index(mais_proximo)
    return dias[indice], mais_proximo

def main():
    visitantes = []

    for dia in ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]:
        while True:
            try:
                numero = int(input(f"Introduza o número de visitantes para {dia}: "))
                if numero >= 0:
                    visitantes.append(numero)
                    break
                else:
                    print("Erro: O número de visitantes não pode ser negativo.")
            except ValueError:
                print("Erro: Entrada inválida. Por favor, introduza um número inteiro.")

    visitantes_decrescentes = listar_visitantes_decrescentes(visitantes)
    
    media = media_visitantes(visitantes)
   
    dia_proximo, visitantes_proximos = dia_mais_proximo_media(visitantes, media)

    print("\nNúmero de visitantes por dia (ordem decrescente):")
    for v in visitantes_decrescentes:
        print(v)
    
    print(f"\nNúmero médio de visitantes por dia: {media:.2f}")
    print(f"O dia que mais se aproximou da média foi {dia_proximo} com {visitantes_proximos} visitantes.")

if __name__ == "__main__":
    main()

def romanNumeral(numero):
    if numero < 1 or numero > 999:
        return "Número deve estar entre 1 e 999."
    
    numero_romano = [
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
    
    resultado = ""

    for valor, simbolo in numero_romano:
        while numero >= valor:
            resultado += simbolo
            numero -= valor
            
    return resultado

numero = int(input("Escreva um número entre 1 e 999: "))
print(romanNumeral(numero))

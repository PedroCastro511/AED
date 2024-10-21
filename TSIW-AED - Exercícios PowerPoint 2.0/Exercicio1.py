def somatorio(num1, num2):

    if num1 > num2:
        num1, num2 = num2, num1
    
    soma = 0
    for i in range(num1, num2 + 1):
        soma += i
    
    print(f"Somatório de {num1} até {num2} é: {soma}")

num1 = int(input("Introduza um numero inteiro: "))
num2 = int(input("Introduza outro inteiro: "))

somatorio(num1, num2)
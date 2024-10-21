numero = int(input("Nº de termos a imprimir: "))

if numero < 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    a, b = 0, 1
    sequenciaFibonacci = [a]

    for _ in range(1, numero):
        sequenciaFibonacci.append(b)
        a, b = b, a + b

    print(f"Primeiros {numero} termos da sequência de Fibonacci são: {sequenciaFibonacci}")

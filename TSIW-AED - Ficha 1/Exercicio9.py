Peso = float(input("Peso (kg): "))
print()
Altura = float(input("Altura (m): "))
print()

IMC = (Peso/(Altura*Altura))

if IMC < 18.5:
    print("O seu IMC é: {:.2f}" .format(IMC))
    print("Baixo Peso")

if IMC >= 18.5 and IMC <= 24.9:
    print("O seu IMC é: {:.2f}" .format(IMC))
    print("Peso normal")

if IMC >= 25 and IMC <= 29.9:
    print("O seu IMC é: {:.2f}" .format(IMC))
    print("Excesso de Peso")

if IMC >= 30 and IMC <= 34.9:
    print("O seu IMC é: {:.2f}" .format(IMC))
    print("Obesidade Grau |")

if IMC >= 35.5 and IMC <= 39.9:
    print("O seu IMC é: {:.2f}" .format(IMC))
    print("Obesidade Grau ||")

if IMC >= 40:
    print("O seu IMC é: {:.2f}" .format(IMC))
    print("Obesidade Mórbida")

input()
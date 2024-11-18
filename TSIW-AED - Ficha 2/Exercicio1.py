numero = int (input("Indique um número: "))
fatorial = 1
numeroFatorial = numero

while numeroFatorial > 1:
      fatorial *= numeroFatorial
      numeroFatorial -= 1

print(f'Fatorial de {numero} = {fatorial}')
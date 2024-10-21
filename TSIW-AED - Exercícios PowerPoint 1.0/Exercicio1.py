i = 0
media = 0
numeroMaior = 0
while i <10:
    numero = int (input("Indique {:n}º numero: " .format(i+1)))
    if numero>20:
        print("Indique somente números inferiores a 20")
        continue
    if numero > numeroMaior:
        numeroMaior = numero
    media+=numero
    i+=1
    

print()
print("A média é {:n}" .format(media/10))
print("O maior número é {:n}" .format(numeroMaior))
print()


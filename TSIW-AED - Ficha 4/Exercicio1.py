def aboveAverage(Listnumero):
    media = sum(Listnumero) / len(Listnumero)
    cont = 0
    for numeros in Listnumero:
        if numeros > media:
            cont+=1
    return cont
  
Listnumero = []
for i in range(10):
    numeros = int(input('Indique o {:n}º número: ' .format(i+1)))
    Listnumero.append(numeros)

cont = aboveAverage(Listnumero)
print('Existem {:n} números acima da média' .format(cont))


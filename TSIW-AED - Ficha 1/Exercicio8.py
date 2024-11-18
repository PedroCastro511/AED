Sexo= str(input("Digite o sexo(M/F): "))    
Altura = float(input("Indique a altura (cm): "))

if Sexo == ("F"):
    k = 2
    Peso_ideal = (Altura-100) - (Altura-150)/k
    print("O Peso Ideal é {:.2f} kg" .format(Peso_ideal))
elif Sexo == ("M"):
    k = 4
    Peso_ideal = (Altura-100) - (Altura-150)/k
    print("O Peso Ideal é {:.2f} kg" .format(Peso_ideal))


input()


numero = int(input("Número: "))

primo = True
for i in range(2, numero):
    resto = numero % i
    if resto == 0:
        primo = False
        break

if primo == True:
    print(f"O {numero} é um número primo.")
else:
    print(f"O {numero} não é um número primo.")




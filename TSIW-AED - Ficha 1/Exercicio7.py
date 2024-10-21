Sexo= str(input("Digite o sexo(M/F): "))
print()
Idade = int(input("Digite a idade: "))
ContaHomem = (220 - (Idade))
ContaMulher = (226 - (Idade))
print()
if Sexo == ("F"):
    print("FCM= {:.2f} bpm" .format(ContaMulher))
elif Sexo == ("M"):
    print("FCM= {:.2f} bpm" .format(ContaHomem))
else:
    print("Indique o seu sexo de forma correta, F ou M")
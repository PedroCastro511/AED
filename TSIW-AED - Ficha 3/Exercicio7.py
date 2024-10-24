import random

def generatePassword(userName):
    if ' ' in userName:
        return "Username é inválido"
    
   
    caracteres_pares = userName[1::2]
    
    password = ""
    for char in caracteres_pares:
        numero_aleatorio = random.randint(1, 9) 
        password += char + str(numero_aleatorio)
    
    password += str(len(userName))
    return password

userName = input("Escreva o seu username: ")
print("Password: " + generatePassword(userName))


segundos =int(input("Indique o tempo em segundos: "))

# o // siginifica o quociente 
horas = segundos // 3600
minutos = (segundos %3600) // 60
segundos_restantes = segundos % 60

print(f"{horas} horas, {minutos} minutos, {segundos_restantes} segundos")
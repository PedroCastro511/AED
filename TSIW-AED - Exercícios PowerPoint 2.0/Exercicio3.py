def heartRate(fc):
    if 50 <= fc <= 80:
        return "treino aeróbico"
    elif 80 < fc <= 100:
        return "treino cardiovascular"
    elif 100 < fc <= 120:
        return "treino aeróbico ideal"
    elif 120 < fc <= 140:
        return "treino anaeróbico"
    else:
        return "Frequência cardíaca fora do intervalo esperado"

    
resultado =heartRate(130) 

print(f'Nível de esforço: {resultado}')

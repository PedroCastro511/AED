from PIL import Image
import os

def criar_bandeira_vertical():
  
    largura, altura = 240, 240

    
    imagem = Image.new("RGB", (largura, altura))
    pixels = imagem.load()

    cores = [(0, 0, 255),  
             (255, 255, 255),  
             (255, 0, 0)] 

    
    for x in range(largura):
        faixa = x // 80 
        cor = cores[faixa]
        for y in range(altura):
            pixels[x, y] = cor

    
    pasta_saida = "images"
    os.makedirs(pasta_saida, exist_ok=True)
    caminho_arquivo = os.path.join(pasta_saida, "bandeira.jpg")
    imagem.save(caminho_arquivo)

    print(f"A imagem da bandeira foi salva em: {caminho_arquivo}")


criar_bandeira_vertical()
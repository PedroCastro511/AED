from PIL import Image
import os

def imageGrayScale(caminho_imagem):
    try:
        imagem = Image.open(caminho_imagem)
        
        imagem = imagem.convert("RGB")

        largura, altura = imagem.size
        nova_imagem = Image.new("L", (largura, altura)) 
        pixels_original = imagem.load()
        pixels_novo = nova_imagem.load()

        for x in range(largura):
            for y in range(altura):
                red, green, blue = pixels_original[x, y]
                gray = int(0.299 * red + 0.587 * green + 0.114 * blue)
                pixels_novo[x, y] = gray

        nova_imagem.show()

        pasta_saida = "images"
        os.makedirs(pasta_saida, exist_ok=True)
        caminho_saida = os.path.join(pasta_saida, "imagem_grayScale.jpg")
        nova_imagem.save(caminho_saida)

        print(f"A imagem em GrayScale foi salva em: {caminho_saida}")

    except FileNotFoundError:
        print(f"Erro: O arquivo {caminho_imagem} não foi encontrado.")
    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")

caminho_da_imagem = "images/bandeira.jpg"
imageGrayScale(caminho_da_imagem)
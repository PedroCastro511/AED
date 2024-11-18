from PIL import Image, ImageOps
import os

def criar_moldura_janela(caminho_imagem):
    try:
        imagem = Image.open(caminho_imagem)

        espessura_moldura = 10

        imagem_com_moldura = ImageOps.expand(imagem, border=espessura_moldura, fill="blue")

        imagem_com_moldura.show()

        pasta_saida = "images"
        os.makedirs(pasta_saida, exist_ok=True)
        caminho_saida = os.path.join(pasta_saida, "imagem_com_moldura_janela.jpg")
        imagem_com_moldura.save(caminho_saida)

        print(f"A imagem com moldura foi salva em: {caminho_saida}")

    except FileNotFoundError:
        print(f"Erro: O arquivo {caminho_imagem} não foi encontrado.")
    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")

caminho_da_imagem = "images/bandeira.jpg"
criar_moldura_janela(caminho_da_imagem)
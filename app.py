import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")

lista_arquivos = os.listdir(caminho)
lista_arquivos.sort()
# print(lista_arquivos)

# /mnt/c/Users/jonat/Downloads/executar
existe_imagem = False
extensao_imagem = []
existe_pdf = False
extensao_pdf = []
existe_planilhas = False
extensao_planilhas = []
existe_documentos = False
extensao_documentos = []
existe_aplicativo = False
extensao_aplicativo = []
existe_musica = False
extensao_musica = []
existe_video = False
extensao_video = []

locais = dict()

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")

    if ".png" in extensao or ".jpeg" in extensao or ".jpg" in extensao:
        existe_imagem = True

        if existe_imagem and extensao not in extensao_imagem:
            extensao_imagem.append(extensao)

    if ".doc" in extensao or ".docx" in extensao:
        existe_documentos = True

        if existe_documentos and extensao not in extensao_documentos:
            extensao_documentos.append(extensao)

    if ".pdf" in extensao:
        existe_pdf = True

        if existe_pdf and extensao not in extensao_pdf:
            extensao_pdf.append(extensao)

    if ".xls" in extensao or ".xlsx" in extensao:
        existe_planilhas = True

        if existe_planilhas and extensao not in extensao_planilhas:
            extensao_planilhas.append(extensao)

    if ".exe" in extensao:
        existe_aplicativo = True

        if existe_aplicativo and extensao not in extensao_aplicativo:
            extensao_aplicativo.append(extensao)

    if ".mp4" in extensao:
        existe_video = True

        if existe_video and extensao not in extensao_video:
            extensao_video.append(extensao)

    if ".mp3" in extensao:
        existe_musica = True

        if existe_musica and extensao not in extensao_musica:
            extensao_musica.append(extensao)


# locais["images"] = []
# locais["images"].extend([extensao])
print(extensao_imagem)
print(extensao_documentos)
print(extensao_aplicativo)
print(extensao_musica)
print(extensao_video)
print(extensao_planilhas)
print(extensao_pdf)

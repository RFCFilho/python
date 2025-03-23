import PyPDF2 #instalara esta biblioteca e importar
import os #este não precisa instalar

merger = PyPDF2.PdfMerger() #mesclador de pdfs

lista_arquivos = os.listdir("arquivos")#esta variável busca na biblioteca OS o listdir que vai listar os pdfs que estão na parata arquivos
lista_arquivos.sort()
print(lista_arquivos)

for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"arquivos/{arquivo}")

merger.write("exerGeral.pdf")





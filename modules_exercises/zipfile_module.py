import os
from zipfile import ZipFile

""" Passa em todos os arquivos de um pasta e 
    compacta tudo em um unico arquivo .zip """
path = r"C:\Users\kaique.silva\Desktop\arquivo"
with ZipFile("arquivo.zip", "w") as zip_file:
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        zip_file.write(full_path, file)
        print(file)

""" Mostra o conteudo de um arquivo zip """
with ZipFile("arquivo.zip", "r") as file:
    for file in file.namelist():
        print(file)

"""Descompacta o arquivo do diretorio atual. """
with ZipFile("arquivo.zip", "r") as file:
    file.extractall("descompactado")

""" Itera sobre cada arquivo da pasta e descompacta cada um. """
unzip_path = r"C:\Users\kaique.silva\DEsktop\python_exercises\descompactado"
for file in os.listdir(unzip_path):
    file = os.path.join(unzip_path, file)
    with ZipFile(f"{file}", "r") as file:
        file.extractall("descompactado02")

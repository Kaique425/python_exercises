import os

caminho = os.getcwd()
total_py = total = tamanho_total = 0
for raiz, diretorio, arquivos in os.walk(caminho):
    total += 1
    for arquivo in arquivos:
        ext: tuple = os.path.splitext(arquivo)
        if ext[1] == ".py":
            total_py += 1
        caminho_completo = os.path.join(raiz, arquivo)
        tamanho = os.path.getsize(caminho_completo)
        tamanho_total += tamanho
        print()
        print(f"Caminho completo: {caminho_completo}")
        print(f"Nome do arquivo: {ext[0]}")
        print(f"Extensão do arquivo {ext[1]}")
        print(f"Tamanho do arquivo {tamanho}")
        print()

print(f"Tamanho total {tamanho_total}")
print(f"Ao total {total} arquivos encontrado(s) ")
print(f"Sendo {total_py} arquivos python")

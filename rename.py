import os

def renomear_arquivos(diretorio):
    # Obtém a lista de arquivos no diretório
    arquivos = os.listdir(diretorio)

    # Itera sobre cada arquivo no diretório
    for arquivo in arquivos:
        # Cria o novo nome de arquivo com "-1" antes da extensão
        novo_nome = os.path.join(diretorio, arquivo[:-len(os.path.splitext(arquivo)[1])] + "-1" + os.path.splitext(arquivo)[1])

        # Renomeia o arquivo
        os.rename(os.path.join(diretorio, arquivo), novo_nome)
        print(f"Arquivo renomeado: {arquivo} para {os.path.basename(novo_nome)}")

# Substitua 'caminho_do_diretorio' pelo caminho do diretório que você deseja renomear
caminho_do_diretorio = r'C:\temp\XMLs Takeda'
renomear_arquivos(caminho_do_diretorio)
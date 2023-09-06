import os
import re

# Defina o diretório onde estão os arquivos XML
diretorio = r'C:\Users\iuri.guelfo\Desktop\xml'

# Defina as datas a serem substituídas e suas correspondentes substituições
substituicoes = [
    ('2023-09-01', '2023-08-31'),
    ('2023-09-02', '2023-08-31'),
    ('2023-09-03', '2023-08-31'),
    ('2023-09-04', '2023-08-31'),
    ('2023-09-05', '2023-08-31'),
    ('2023-09-06', '2023-08-31'),
    # Adicione mais datas e substituições conforme necessário
]


# Função para substituir as datas em um arquivo
def substituir_datas_em_arquivo(caminho_arquivo, substituicoes):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()

        # Aplicar todas as substituições no conteúdo do arquivo
        for substituicao in substituicoes:
            data_substituida, data_substituta = substituicao
            conteudo = re.sub(data_substituida, data_substituta, conteudo)

        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudo)

        print(f'Arquivo {caminho_arquivo} processado com sucesso.')

    except Exception as e:
        print(f'Erro ao processar o arquivo {caminho_arquivo}: {str(e)}')


# Iterar sobre todos os arquivos na pasta
for raiz, _, arquivos in os.walk(diretorio):
    for arquivo in arquivos:
        if arquivo.endswith('.xml'):
            caminho_arquivo = os.path.join(raiz, arquivo)
            substituir_datas_em_arquivo(caminho_arquivo, substituicoes)

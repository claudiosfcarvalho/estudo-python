# intermediario/arquivos.py
# Leitura e escrita de arquivos texto
import os
# Diretório onde será criado o arquivo
pasta_saida = "saida_teste"

# Cria a pasta se ela não existir
os.makedirs(pasta_saida, exist_ok=True)

# Monta o caminho completo para o arquivo
caminho = os.path.join(pasta_saida, "dados.txt")

# Escrevendo no arquivo
with open(caminho, "w", encoding="utf-8") as f:
    f.write("Linha 1\n")
    f.write("Linha 2\n")

# Lendo o arquivo
with open(caminho, "r", encoding="utf-8") as f:
    for linha in f:
        print("Conteúdo:", linha.strip())

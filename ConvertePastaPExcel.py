import os
import csv
import openpyxl

# Pedir ao usuário o caminho da pasta e a lista de cabeçalhos
pasta = input("Digite o caminho da pasta: ")
cabecalhos = input("Digite a lista de cabeçalhos separados por vírgulas: ").split(",")

# Criar um objeto Workbook do openpyxl
workbook = openpyxl.Workbook()
# Iterar sobre todos os arquivos na pasta
for filename in os.listdir(pasta):
    if filename.endswith(".txt"):
        # Abrir o arquivo texto
        with open(os.path.join(pasta, filename), "r") as arquivo:
            # Ler o conteúdo do arquivo e dividir em linhas
            conteudo = arquivo.read()
            linhas = conteudo.split("\n")
            # Criar um objeto Worksheet do openpyxl com o nome
            worksheet = workbook.create_sheet(title=filename)
            # Adicionar os cabeçalhos à primeira linha da planilha
            worksheet.append(cabecalhos)
            # Adicionar as linhas restantes à planilha
            for linha in linhas:
                valores = linha.split(";")
                worksheet.append(valores)
# Salvar o arquivo Excel
workbook.save("resultado.xlsx")

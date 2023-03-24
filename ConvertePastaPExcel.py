import os
import csv
import openpyxl

# Pedir ao usuário o caminho da pasta e a lista de cabeçalhos
pasta = input("Digite o caminho da pasta com os arquivos gerados pelo toad: ")
script_base = input("Digite o caminho e nome  da script  SQL: ")

def cria_cabecalho(script_base):
   #C:\Users\e070800\OneDrive - Mastercard\Documents\Python\Gerenciar Arquivos com Python
    lista = []
    with open(os.path.join(script_base), "r") as arquivo:
        conteudo = arquivo.read()
        linhas = conteudo.split("\n")
        for item in linhas:
            inicio = item.find('"') + len('"')
            fim = item.find('"', inicio)
            if inicio >= 0 and fim >= 0 and  item[inicio:fim]  != ';':
                print(item[inicio:fim])
                lista += [item[inicio:fim]]
    return lista
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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
            cabecalhos = cria_cabecalho(script_base)
            worksheet.append(cabecalhos)
            # Adicionar as linhas restantes à planilha
            for linha in linhas:
                valores = linha.split(";")
                worksheet.append(valores)
# Salvar o arquivo Excel
workbook.save("resultado.xlsx")

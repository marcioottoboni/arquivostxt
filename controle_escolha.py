escolha = input('Digite 1 para gerar 2 para processar e 3 para sair: ')

def escolha_01(parametro):
    print(f'Chamou a funcao {parametro} ')
def escolha_02(parametro):
    print(f'Chamou a funcao {parametro} ')
while escolha != '3':
    if escolha == '1':
        print(f'A escolha do usuario foi {escolha}')
        parametro = escolha
        escolha_01(parametro)
        escolha = input('Digite 1 para gerar 2 para processar e 3 para sair')
    elif escolha == '2':
        print(f'A escolha do usuario foi {escolha}')
        parametro = escolha
        escolha_02(parametro)
        escolha = input('Digite 1 para gerar 2 para processar e 3 para sair')
    else:
        print(f'Digite 1,2 ou 3 !!')
        escolha = input('Digite 1 para gerar 2 para processar e 3 para sair')
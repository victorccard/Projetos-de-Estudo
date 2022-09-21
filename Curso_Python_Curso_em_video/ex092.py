from time import sleep
dados = {}
dados['nome'] = str(input('Nome: '))
dados['Nasc'] = int(input('Ano de Nascimento: '))
dados['carteira'] = int(input('Carteira de trabalho ( 0 não tem): '))
if dados['carteira'] != 0:
    dados['Contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = int(input('Salário: R$ '))
print('-=' * 30)
for k, v in dados.items():
    print(f'- {k} tem o valor {v}')
    sleep(1)

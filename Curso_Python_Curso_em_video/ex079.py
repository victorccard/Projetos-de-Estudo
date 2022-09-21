valores = list()
while True:
    v = int(input('Digite um valor: '))
    if v not in valores:
        valores.append(v)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor Duplicado! Não vou adicionar...')
    cont = str(input('Quer continuar? [s/n} '))
    if cont in 'nN':
        break
valores.sort()
print(f'Você digitou os valores {valores}')

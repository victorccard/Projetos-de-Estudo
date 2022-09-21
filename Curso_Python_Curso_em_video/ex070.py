"""
Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar.
"""

print('-'*30)
print('{: ^30}'.format('LOJA SUPER BARATÃO'))
print('-'*30)

prodcaros = totpreço = menor = cont = 0
barato = ' '
while True:
    prod = str(input('Nome do produto: '))
    preço = int(input('Preço: R$ '))
    cont += 1
    totpreço += preço
    if preço > 1000:
        prodcaros += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = prod
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if res == 'N':
        break
print(f'O total da compra foi R${totpreço}')
print(f'Temos {prodcaros} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}')


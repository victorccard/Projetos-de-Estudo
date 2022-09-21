def area(a, b):
    ar = a * b
    print(f'A área de um terreno de {a}x{b} é de {ar}m²')


print()
print('Controle de terrenos')
print('-'*20)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)

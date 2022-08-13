lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    c = str(input('Quer continuar? [S/N]'))
    if c in 'Nn':
        break
print(f'A Lista completa é {lista}')
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(i)
print(f'A Lista pares é {pares}')
print(f'A Lista impares é {impares}')

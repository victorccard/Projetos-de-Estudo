lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    c = str(input('Quer continuar? [S/N]'))
    if c in 'Nn':
        break
print(f'Você digitou {(len(lista))} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')

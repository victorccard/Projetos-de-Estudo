"""Faça uma tabuada de um número que o
usuário escolher ultilizando loop for"""
n = int(input('Digite um número: '))
for tab in range(1, 11):
    print('-'*12)
    print( '{} x {:2} = {}'.format(n, tab, n*tab))
print('-'*12)
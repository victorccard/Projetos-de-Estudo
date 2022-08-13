"""
Faça um programa que mostre a tabuada de vários números, um de cada vez
para cada valor digitado pelo usuário. O programa será interrompido
quando o número solicitado for negativo.
"""

tab = 0
while True:
    num = int(input('Quer ver a tabuada de qual valor?'))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')



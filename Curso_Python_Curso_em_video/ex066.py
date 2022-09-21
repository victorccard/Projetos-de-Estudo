"""
Crie um programa que leia vários números. O programa só vai parar quando o usuário digitar '999'. No final
mostre quantos números foram digitados e qual foi a soma entre eles.
"""
soma = c = 0
while True:
    num = int(input('Digite um valor(999 para parar):'))
    if num == 999:
        break
    soma += num
    c += 1
print(f'A soma dos {c} valores é igual a {soma}')


"""
Crie um programa que leia dois valores e mostre um menu como o ao lado
na tela:
Seu programa deverá realizar a operação solicitada em cada caso.
"""

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print("""
            [1] SOMAR
            [2] MULTIPLICAR
            [3] MAIOR
            [4] NOVOS NÚMEROS
            [5] SAIR DO PROGRAMA """)
    opcao = int(input('Qual é a sua opção?'))
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} + {} = {}'.format(n1, n2, soma))
    elif opcao == 2:
        multiplicar = n1 * n2
        print('A multiplicação de {} * {} = {} '.format(n1, n2, multiplicar))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('O maior número é {}'.format(maior))
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida. Tente novamente')
    print('=-='*10)
print('Fim do programa! Volte sempre!')

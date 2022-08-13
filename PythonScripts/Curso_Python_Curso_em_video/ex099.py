from time import sleep


def analise(* num):
    cont = maior = 0
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print()
    print('-='*25)
    print('Analisando os valores passados...')
    print(f'{num} Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


analise(1, 2, 3, 4)
analise(4, 7, 0)
analise(3, 6)

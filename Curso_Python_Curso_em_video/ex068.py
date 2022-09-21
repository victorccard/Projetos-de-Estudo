import random
v = 0
while True:
    print('=-'*15)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('=-'*15)
    jogn = int(input('Diga um valor: '))
    compn = random.randint(0, 10)
    tipo = ' '
    total = jogn + compn
    while tipo not in 'PI':
        tipo = str(input("Par ou ímpar? [P/I] ")).strip().upper()[0]
    print(f'Você jogou {jogn} e o computador {compn}. Total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes')

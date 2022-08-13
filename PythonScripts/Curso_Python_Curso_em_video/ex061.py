"""
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
Mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""
print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão da PA: '))
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} =>'.format(termo), end='')
        termo += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais:'))
print('Progressão finalizada com {} termos mostrados.'.format(total))

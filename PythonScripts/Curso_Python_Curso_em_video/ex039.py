from datetime import date
nasc = int(input('Ano de nascimento:'))
atual = date.today().year
idade = atual - nasc
alist = 18 - idade
anoalist = atual - alist
print('Quem nasceu em {} tem {} em 2022'.format(nasc, idade))
if idade < 18:
    print('Ainda Faltam {} anos para o alistamento militar'.format(alist))
    print('Seu alistamento será em {}'.format(anoalist))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(alist))
    print('Seu alistamento foi em {}'.format(anoalist))
else:
    print('Você tem que se alistar IMEDIATAMENTE')
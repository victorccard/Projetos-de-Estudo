sal = float(input('Qual é o salário do funcionário? R$'))
if sal <= 1250:
    aum = sal + (sal * 15 / 100)
else:
    aum = sal + (sal * 10 / 100)
print('Quem ganhava R$ {} passa a ganhar R$ {} agora.'.format(sal, aum))
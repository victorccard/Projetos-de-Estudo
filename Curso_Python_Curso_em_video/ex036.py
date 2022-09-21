casa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
ano = int(input('Quantos anos de financiamento:'))
prescomp = sal * 30/100
presfin = casa / (ano * 12)
print('Para pagar uma casa no valor de {:.2f} R$ em  {} anos a prestação será de R${:.2f}'.format(casa, ano, presfin))
if prescomp > presfin:
    print('Financiamento CONCEDIDO')
else:
    print('FInanciamento NEGADO')
print('E a sua prestação é de {}'.format(presfin))
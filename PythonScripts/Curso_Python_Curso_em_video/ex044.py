# noinspection PyStringFormat
print('{:=^40}'.format('LOJAS CARDOSO'))
pag = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinherio/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
o = int(input('Qual é a opção?'))
if o == 1:
    total = pag - (pag * 0.10)
elif o == 2:
    total = pag - (pag * 0.05)
elif o == 3:
    total = pag
    p = pag / 2
    print('Você vai pagar em 2x {}'.format(p))
elif o == 4:
    p = int(input('Quantas parcelas?'))
    total = pag + (pag * 0.20)
    print('Sua compra será parcelada em {}x de {} COM JUROS'.format(p, pag))
else:
    total = 0
    print('OPÇÃO INVÁLIDA')
print('Sua compra de {:.2f} vai custar R${:.2f} no final.'.format(pag, total))















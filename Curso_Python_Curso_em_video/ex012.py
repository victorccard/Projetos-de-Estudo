preço = float(input('Qual é o preço do produto: R$'))
novo = preço - (preço*5/100)
print('O valor com desconto de 5% é de {:.2f}'.format(novo))
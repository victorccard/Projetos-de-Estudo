import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R${p} é R$ {moeda.metade(p)}')
print(f'O dobro de R${p} é R$ {moeda.dobro(p)}')
print(f'Aumentando 10%, temos R$ {moeda.aumento(p, 10)}')

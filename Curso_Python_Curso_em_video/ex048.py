"""Faça um programa que calcule a soma entre todos
os números impares que são múltiplos de três e
que se encontram no intervalo de 1 a 500."""
soma = 0   # Acumulador
cont = 0   # Contador
for c in range(1, 501, 2):
    if c % 3 == 0:                  # c é divisivel por 3 #
        soma = soma + c     # Acumulador
        cont = cont + 1     # Contador
print('Foram descobertos {} números e a soma de todos os valores é {}'.format(cont, soma))


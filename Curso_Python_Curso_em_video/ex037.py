num = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opcção = int(input('Sua opção: '))
if opcção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcção == 2:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, oct(num)[2:]))
elif opcção == 3:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente Novamente.')
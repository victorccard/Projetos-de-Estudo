maisdezoito = 0
homem = 0
mulhermenor = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        maisdezoito += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulhermenor += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if cont == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {maisdezoito}')
print(f'Ao todo temos {homem} homens cadastrado')
print(f'E temos {mulhermenor} Mulheres com menos de 20 anos')

def metade(preco, formato=False):
    met = preco / 2
    return met if formato is False else moeda(met)


def dobro(preco, formato=False):
    dob = preco * 2
    return dob if formato is False else moeda(dob)


def aumento(preco, taxa, formato=False):
    aum = preco + (preco * taxa / 100)
    return aum if formato is False else moeda(aum)


def diminuir(preco, taxa, formato=False):
    dim = preco - (preco + taxa / 100)
    return dim if formato is False else moeda(dim)


def moeda(preco = 0, moeda ='R$'):
    return f'{moeda}{preco:4.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t\t{moeda(preco)}')
    print(f'Dobro do preço: \t\t{dobro(preco, True)}')
    print(f'Metade do preço: \t\t{metade(preco, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumento(preco, taxaa, True)}')
    print(f'Com {taxar}% de redução: \t\t{diminuir(preco, taxar, True)}')
    print('-'*30)
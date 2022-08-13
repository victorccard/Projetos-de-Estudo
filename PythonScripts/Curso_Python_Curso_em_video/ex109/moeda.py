def metade(n, formato=False):
    met = n / 2
    return met if formato is False else moeda(met)


def dobro(n, formato=False):
    dob = n * 2
    return dob if formato is False else moeda(dob)


def aumento(n, taxas, formato=False):
    aum = n + (n * taxas/100)
    return aum if formato is False else moeda(aum)


def dimunir(n, taxas, formato=False):
    dim = n - (n + taxas/100)
    return dim if formato is False else moeda(dim)


def moeda(preco = 0, moeda ='R$'):
    return f'{moeda}{preco:4.2f}'.replace('.', ',')

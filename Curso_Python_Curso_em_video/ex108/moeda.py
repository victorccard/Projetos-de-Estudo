def metade(n):
    met = int(n / 2)
    return met


def dobro(n):
    dob = int(n * 2)
    return dob


def aumento(n, taxas):
    aum = n + (n * taxas/100)
    return aum


def dimunir(n, taxas):
    dim = n - (n + taxas/100)
    return dim


def moeda(preco = 0, moeda ='R$'):
    return f'{moeda}{preco:4.2f}'.replace('.', ',')

n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
m = (n1 + n2) / 2
if m >= 7:
    print('Tirando {:.1f} e {:1f}, a média do aluno é {}'.format(n1, n2, m))
    print('O aluno está APROVADO')
elif m >= 5  and m <= 6.9:
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {}'.format(n1, n2, m))
    print('O aluno está em RECUPERAÇÃO')
else:
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, m))
    print('O aluno está em REPROVADO')
print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
n0 = int(input('Primeiro Termo:'))
r = int(input('Razão:'))
n10 = n0 + (10 - 1) * r
for c in range(n0, n10 + r, r):
    print('{}'.format(c), end=' - ')
print('ACABOU')

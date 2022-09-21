from math import hypot
opos = float(input('Comprimento do cateto oposto: '))
adj = float(input('Comprimento do cateto adjacente: '))
hip = hypot(opos, adj)
print('A hipotenusa vai medir {:0}'.format(hip))
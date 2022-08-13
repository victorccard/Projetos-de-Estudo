jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou:? '))
for c in range(0, tot):
    gols.append(int(input(f'   Quantos gols na partida  {c}?')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for c, v in jogador.items():
    print(f'O campo {c} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {tot}')
for p, d in enumerate(jogador['gols']):
    print(f'=> Na partida {p}, fez {d} gols')
print(f'Foi um total de {jogador["total"]} gols.')

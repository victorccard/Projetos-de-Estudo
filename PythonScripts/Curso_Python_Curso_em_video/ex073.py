'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do
Brasileirão na ordem de colocação.'''

times = ('Coritinhias', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
             'Palmeiras', 'Santos', 'Grêmio', 'São Paulo', 'Fluminense', 'Sport Recife',
             'EC Vitória', 'Coritiba', 'Avai', 'Ponte Preta', 'Bahia', 'Atleico PR',
             'Atletico MG', 'Botafogo', 'Nautico')
print('-='*15)
print(f'Lista de times do Brasileirão: {times}')
print('-='*15)
print(f'os 5 primeiros são {times[0:5]}')
print('-='*15)
print(f'os 5 ultimos são {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética {sorted(times)}')
print('-='*15)
print(f'O chapecoense está na {times.index("Chapecoense") + 1}')
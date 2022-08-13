vel = int(input('Qual a velocidade atual do carro?'))
valor = (vel-60) * 7
if vel <= 60:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('Multado! Excedeu o limite de velocidade que é de 80Km/h')
    print('Você deve pagar uma multa de {}!'.format(valor))
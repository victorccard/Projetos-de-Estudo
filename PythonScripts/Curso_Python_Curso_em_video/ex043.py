p = float(input('Qual é seu peso? (Kg)'))
a = float(input('Qual é seu altura? (m)'))
IMC = p / (a * a)
print('O IMC dessa pessoa é de {:.2f}'.format(IMC))
if IMC < 18.5:
    print('Você está ABAIXO DO PESO')
elif IMC < 25:
    print('PARANBÉNS! Você está no peso ideal')
elif IMC < 30:
    print('Você está em SOBREPESO')
elif IMC < 40:
    print('Cuidado! Vocé está com OBESIDADE')
elif IMC > 40:
    print('CUIDADO! Vocé está com OBESIDADE MORBIDA')

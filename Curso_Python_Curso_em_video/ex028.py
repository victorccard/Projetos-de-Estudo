import random
import time
ran = random.randint(1,5)
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. tente adivinhar...')
print('-=-' * 20)
n = int(input('Em que número eu estou pensando? '))
print('PROCESSANDO...')
time.sleep(1)
if ran == n:
    print('PARABÉNS!!! Você ganhou!')
else:
    print('Você errou! O número que pensei foi {}. Mas sorte na próxima vez!'.format(ran))


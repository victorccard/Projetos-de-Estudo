l = int(input('Largura da parede: M'))
h = int(input(' Altura da parede: M'))
a = int(l * h)

print('Sua parede tem a dimensão de {}x{} e sua área é de {}.'.format(l,h,a))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(a / 2))
import math
ang = float(input('Digite o valor do ângulo: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print('O ângulo de {} tem o seno de {:.2f}, cosseno de {:.2f} e tangente de {:.2f}'.format(ang, seno, cosseno, tangente))


from math import hypot
ca = float(input('Digite o comprimento do cateto adjacente: '))
co = float(input('Digite o comprimento do cateto oposto: '))
hi = hypot(ca, co)
print('O valor da hipotenusa é {}'.format(hi))


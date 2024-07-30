# FATORIAL USANDO WHILE
n = int(input("Digite um valor: "))
n2 = n
fatorial = 1
while n > 0:
    fatorial *= n
    n -= 1
print("O fatorial de {} é {}".format(n2, fatorial))

'''
FATORIAL USANDO FOR
n = int(input("Digite um valor: "))
n2 = n
fatorial = 1
for n in range(n, 0, -1):
    fatorial *= n
print("O fatorial de {} é {}".format(n2, fatorial))
'''
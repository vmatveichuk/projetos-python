s = 0
for c in range(1, 7):
    n = int(input("Digite o {}° valor: ".format(c)))
    if n % 2 == 0:
        s += n
print("O soma entre os pares é {}".format(s))



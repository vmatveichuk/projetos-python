a = list()
while True:
    a.append(int(input("Digite um valor: ")))
    opcao = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if opcao in "N":
        break
    while opcao not in "SN":
        opcao = str(input("Dígito inválido, Quer continuar? [S/N] ")).upper().strip()[0]
    if opcao in "N":
            break
b = list()
c = list()
for l in a:
    if l % 2 == 0:
        b.append(l)
    else:
        c.append(l)
print(f"A lista com todos números é {a}")
print(f"Os números pares da lista são {b}")
print(f"Os números impares da lista são {c}")

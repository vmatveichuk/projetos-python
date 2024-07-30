n = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f"Digite o {c}° valor: "))
    if valor % 2 == 0:
        n[0].append(valor)
    else:
        n[1].append(valor)
print(f"A lista dos valores pares em ordem crescente são: {sorted(n[0])}")
print(f"A lista dos valores ímpares em ordem crescente são: {sorted(n[1])}")

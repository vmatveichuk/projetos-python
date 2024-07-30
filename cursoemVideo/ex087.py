matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = scol = maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}] [{c}]: "))

print(20 * "=-=")
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if l == 1 and c == 0:
            matriz[1][0] = maior
        else:
            if matriz[1][c] > maior:
                maior = matriz[1][c]
    print()
for l in range(0, 3):
    scol += matriz[l][2]
print(20 * "=-=")
print(f"A soma entre os números pares da matriz é {soma}")
print(f"A soma dos valores da terceira coluna é {scol}")
print(f"O maior valor da segunda linha é {maior}")

def CalculaListaDeColunas(matriz):
    sum_matrix = {}
    for x in range(len(matriz)):
        y_f = ''
        for y in range(len(matriz[x])):
            if not y in sum_matrix:
                sum_matrix[y] = 0
            sum_matrix[y] += matriz[x][y]

    return [s for _, s in sum_matrix.items()]


def CalculaTotal(matriz_sum):
    total = 0
    for i in matriz_sum:
        total += i
    return total


matriz = []
matriz_x = 5
matriz_y = 5

for x in range(matriz_x):
    matriz_2 = []
    for y in range(matriz_y):
        val = input(f"Digite a posição {x}X{y}: ")
        matriz_2.append(int(val if len(val) > 0 else 0))

    matriz.append(matriz_2)

# Exibir Matriz
for x in range(len(matriz)):
    linha = ''
    for y in range(len(matriz[x])):
        linha += f"{matriz[x][y]}   "
    print(linha)

total_colunas = CalculaListaDeColunas(matriz)
total = CalculaTotal(total_colunas)

# Exibir Total Colunas
print("|   " * len(total_colunas))
print("   ".join(str(t) for t in total_colunas))

# Exibir Total Matriz
print(f"\nTotal Matriz: {total}")



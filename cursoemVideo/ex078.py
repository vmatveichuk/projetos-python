lista = list()
maior = menor = 0

for cont in range(0, 5):
    lista.append(int(input(f"Digite um valor para a posição {cont}: ")))
    if cont == 0:
        maior = lista[cont]
        menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]
print(f"Você digitou os valores {lista}")
print(f"O maior valor digitado foi {maior} nas posições ", end="")
for i, v in enumerate(lista):
    if v == maior:
        print(f"{i}...", end="")
print()
print(f"O menor valor digitado foi {menor} nas posições ", end="")
for i, v in enumerate(lista):
    if v == menor:
        print(f"{i}...", end="")
print()

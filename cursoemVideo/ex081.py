lista = list()
while True:
    lista.append(int(input("Digite um valor: ")))
    opcao = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if opcao in "N":
        break
    while opcao not in "SN":
        opcao = str(input("Dígito inválido, Quer continuar? [S/N] ")).upper().strip()[0]
    if opcao in "N":
            break
print(f"Foram digitados {len(lista)} números")
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print("O 5 está na lista")
else:
    print("O 5 não está na lista")

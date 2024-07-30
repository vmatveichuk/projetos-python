lista = list()
while True:
    n = int(input("Digite um número: "))
    if n not in lista:
        lista.append(n)
        print("Número adicionado com sucesso")
    else:
        print("Número duplicado! Não vou adicionar")
    opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if opcao in "N":
        break
    while opcao not in "SN":
        opcao = str(input("Dígito inválido, Quer continuar? [S/N] ")).upper().strip()[0]
    if opcao in "N":
            break
print("Os números da lista são {}".format(sorted(lista)))


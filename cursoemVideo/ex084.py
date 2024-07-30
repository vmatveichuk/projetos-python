temp = list()
pessoas = list()
tot = 0
maiorpeso = menorpeso = 0
while True:
    temp.append(str(input("Nome: ")))
    temp.append(int(input("Peso: ")))
    tot += 1
    if tot == 1:
        maiorpeso = temp[1]
        menorpeso = temp[1]
    else:
        if temp[1] > maiorpeso:
            maiorpeso = temp[1]
        if temp[1] < menorpeso:
            menorpeso = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    opcao = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if opcao in "N":
        break
    while opcao not in "SN":
        opcao = str(input("Dígito inválido, Quer continuar? [S/N] ")).upper().strip()[0]
    if opcao in "N":
            break
print(f"Ao todo, você cadastrou {tot} pessoas")
print(f"O maior peso foi de {maiorpeso}Kg. Peso de ", end= "")
for p in pessoas:
    if p[1] == maiorpeso:
        print(f"{p[0]}", end=" ")
print(f"\nO menor peso foi de {menorpeso}Kg. Peso de ", end="")
for p in pessoas:
    if p[1] == menorpeso:
        print(f"{p[0]}", end=" ")

somaidade = 0
mediaidade = 0
cont = 0
idadevelho = 0
nomevelho = ""
for c in range(1, 5):
    print("----- {}ª PESSOA -----".format(c))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()
    somaidade += idade
    if sexo == "M":
        if c == 1:
            idadevelho = idade
            nomevelho = nome
        else:
            if idade > idadevelho:
                idadevelho = idade
                nomevelho = nome
    if sexo == "F" and idade < 20:
        cont += 1

mediaidade = (somaidade / 4)
print("A média de idade do grupo é de {} anos".format(mediaidade))
if sexo == "M":
    print("O homem mais velho tem {} anos e se chama {}".format(idadevelho, nomevelho))
else:
    print("Não existem homens solicitados")
print("Existe(m) {} muher(es) com men(os) de 20 anos".format(cont))

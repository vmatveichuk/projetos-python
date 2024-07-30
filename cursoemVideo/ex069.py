cont_idade = 0
cont_homem = 0
cont_mulher_idade = 0
print(20 * "-=-")
print("\33[1;31mCADASTRO DE PESSOAS\33[m")
print(20 * "-=-")

while True:
    idade = int(input("Idade: "))
    sexo = ""
    while sexo != "M" or sexo != "F":
        sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
        if sexo == "M" or sexo == "F":
            break
    opcao = ""
    while opcao != "S" or opcao != "N":
        opcao = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
        if opcao == "S" or opcao == "N":
            break
    if opcao in "Nn":
        break
    if idade >= 18:
        cont_idade += 1
    if sexo in "Mm":
        cont_homem += 1
    if sexo in "Ff":
        if idade < 20:
            cont_mulher_idade += 1
print("Existem {} pessoas que tem mais de 18 anos".format(cont_idade))
print("Foram cadastrados {} homens".format(cont_homem))
print("Existem {} mulheres com menos de 20 anos".format(cont_mulher_idade))


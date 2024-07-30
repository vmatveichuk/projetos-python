print(20 * "-=-")
print("LOJA SUPER BARATÃO")
print(20 * "-=-")
tot_compra = 0
p = 0
cont = 0
menor = 0
menor_nome = ""
while True:
    nome = str(input("Digite o nome do produto: ")).strip().title()
    preco = float(input("Digite o preço do produto: R$"))
    opcao = ""
    while opcao != "S" or opcao != "N":
        opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if opcao == "S" or opcao == "N":
            break
    if opcao == "N":
        break
    cont += 1
    tot_compra += preco
    if preco > 1000:
        p += 1
    if cont == 1:
        menor = preco
        menor_nome = nome
    else:
        if preco < menor:
            menor = preco
            menor_nome = nome
print("O total da compra foi R${:.2f}".format(tot_compra))
print("Temos {} produtos custando mais de R$1000.00".format(p))
print("O produto mais barato foi {} que custa R${:.2f}".format(menor_nome, menor))

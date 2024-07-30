casa = float(input("Digite o valor da casa em R$: "))
sal = float(input("Digite o seu salário em R$: "))
ano = float(input("Digite a quantidade de anos do pagamento: "))
valor = casa / (ano * 12)
if valor > sal * 0.30:
    print("O valor da prestação de R${:.2f} excedeu mais de 30% do seu salário, portanto não poderá realizar a prestação".format(valor))
else:
    print("A prestação foi aprovado e o valor é de R${:.2f} por mês".format(valor))

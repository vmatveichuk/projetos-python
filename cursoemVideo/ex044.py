p = float(input("Digite o preço do produto em R$: "))
print("Digite 1 para pagamento à vista: dinheiro/cheque com 10% de desconto")
print("Digite 2 para pagamento à vista: cartão com 5% de desconto")
print("Digite 3 para pagamento em até 2x no cartão")
print("Digite 4 para pagamento em 3x ou mais no cartão: 20 % de juros")
c = int(input("Digite a condição de pagamento: "))

if c == 1:
    print("O valor a ser pago é de R${:.2f}".format(p*0.90))
elif c == 2:
    print("O valor a ser pago é de R${:.2f}".format(p*0.95))
elif c == 3:
    print("O valor a ser pago por mês é de R${:.2f}".format(p/2))
elif c == 4:
    m = int(input("Digite a quantidade de parcelas: "))
    print("O valor a ser pago por mês é de R${:.2f}".format((p*1.20)/m))
else:
    print("Não existe essa opção")

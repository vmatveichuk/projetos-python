sal = float(input("Digite o salário do funcionário em R$: "))
if sal > 1250:
    print("O salário do funcionário que era R${:.2f}, com o aumento de 10% foi para {:.2f}".format(sal, sal*1.10))
else:
    print("O salário do funcionário que era R${:.2f}, com o aumento de 15% foi para {:.2f}".format(sal, sal * 1.15))

n = int(input("Digite um valor: "))
print("Digite 1 para base binária")
print("Digite 2 para base octal")
print("Digite 3 para hexadecimal")
base = int(input("Digite a base que você deseja converter o valor: "))

if base == 1:
    print("{} convertido para a base binária é igual a {}".format(n, bin(n)))
elif base == 2:
    print("{} convertido para a base octal é igual a {}".format(n, oct(n)))
elif base == 3:
    print("{} convertido para a base hexadecimal é igual a {}".format(n, hex(n)))
else:
    print("Opção inválida, tente novamente")

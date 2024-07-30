n1 = float(input("Digite a 1° nota: "))
n2 = float(input("Digite a 2° nota: "))
media = (n1 + n2) / 2
print("Sua média final foi de {}".format(media))
if media < 5.0:
    print("\33[1;31mREPROVADO\33[m")
elif 6.9 >= media >= 5.0:
    print("\33[1;32mRECUPERAÇÃO\33[m")
else:
    print("\33[1;32mAPROVADO\33[m")


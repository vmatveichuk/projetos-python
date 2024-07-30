p = int(input("Digite o 1° termo da PA: "))
r = int(input("Digite a razão: "))
termo = p
cont = 1
while cont <=10:
    print("{} -> ".format(termo), end="")
    termo += r
    cont += 1
print("FIM")

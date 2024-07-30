a = int(input("Digite o 1° valor: "))
b = int(input("Digite o 2° valor: "))
c = int(input("Digite o 3° valor: "))

while a <= 1:
    print("o valor de a deve ser maior que 1")
    a = int(input("Digite o 1° valor novamente: "))


def Soma(b, c):
    for num in (b, c):
        if b % a == 0 and c % a == 0:
            resultado = b + c
    return resultado


if b % a != 0 or c % a != 0:
    print("b ou c não são divisíveis por a")

else:
    print("A soma entre b e c é {}".format(Soma(b, c)))

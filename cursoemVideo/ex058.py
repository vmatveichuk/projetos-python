import random
usuario = int(input("Digite um valor entre 0 e 10: "))
pc = random.randint(0, 10)
print("Seu número: {}".format(usuario))

c = 0
while usuario != pc:
    print("Computador venceu")
    if usuario > pc:
        print("Menos... tente mais uma vez")
        usuario = int(input("Digite um valor entre 0 e 10: "))
    elif usuario < pc:
        print("Mais... tente mais uma vez")
        usuario = int(input("Digite um valor entre 0 e 10: "))
    c += 1

if usuario == pc:
    print("Número do computador: {}".format(pc))
    print("Você jogou {} vezes para vencer o computador".format(c))
    print("Parabéns, você venceu!!!")

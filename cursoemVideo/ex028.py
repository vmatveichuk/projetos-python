import random
usuario = int(input("Digite um valor entre 0 e 1: "))
pc = random.randint(0, 5)
print("Número do computador: {}".format(pc))
print("Seu número: {}".format(usuario))
if usuario == pc:
    print("Parabéns, você venceu")
else:
    print("Computador venceu, mais sorte da próxima vez")

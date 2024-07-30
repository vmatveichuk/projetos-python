from random import choice
from time import sleep

lista = ["pedra", "papel", "tesoura"]
c = choice(lista)
print("Digite 1 para escolher pedra")
print("Digite 2 para escolher papel")
print("Digite 3 para escolher tesoura")
u = int(input("Faça a sua escolha: "))
print("\33[1;34mJO\33[m")
sleep(1)
print("\33[1;32mKEN\33[m")
sleep(1)
print("\33[1;31mPO!!!\33[m")
print("O computador escolheu {}".format(c))

if u == 1 and c == lista[0]:
    print("Empatou, jogue de novo")
elif u == 2 and c == lista[0]:
    print("Você ganhou, parabéns!!!")
elif u == 3 and c == lista[0]:
    print("Você perdeu, tente novamente")
elif u == 1 and c == lista[1]:
    print("Você perdeu, tente novamente")
elif u == 2 and c == lista[1]:
    print("Empatou, jogue de novo")
elif u == 3 and c == lista[1]:
    print("Você ganhou, parabéns!!!")
elif u == 1 and c == lista[2]:
    print("Você ganhou, parabéns!!!")
elif u == 2 and c == lista[2]:
    print("Você perdeu, tente novamente")
elif u == 3 and c == lista[2]:
    print("Empatou, jogue de novo")
else:
    print("Você não escolheu nenhuma das opções, tente novamente escolhendo pedra, papel ou tesoura")

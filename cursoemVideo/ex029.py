vel = float(input("Digite a velocidade do carro em Km/h: "))
multa = (vel - 80) * 7
if vel > 80:
    print("Você foi multado, pois ultrapassou a velocidade máxima")
    print("Sua multa foi de R${:.2f}".format(multa))
else:
    print("Você está dentro da velocidade permitida")
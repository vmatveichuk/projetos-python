from math import pow

peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura**2)
print("Seu IMC é de {:.2f}".format(imc))
if imc < 18.5:
    print("Abaixo do peso")
elif 25 > imc >= 18.5:
    print("Peso ideal")
elif 30 > imc >= 25:
    print("Sobrepeso")
elif 40 > imc >= 30:
    print("Obesidade")
else:
    print("Obesidade mórbida")

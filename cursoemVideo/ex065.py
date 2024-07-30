resp = "S"
media = 0
cont = 0
maior = menor = 0
soma = 0
while resp in "Ss":
    n = int(input("Digite um número: "))
    resp = str(input("Quer continuar? [S/N] ")).strip().upper()
    cont += 1
    soma += n
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma/cont
print("A média entre os {} números foi {:.2f}".format(cont, media))
print("O maior valor entre eles é {} e o menor valor é {}".format(maior, menor))
print("Acabou")

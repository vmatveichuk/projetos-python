dis = float(input("Digite a distância de uma viagem em Km: "))
if dis <= 200:
    print("O preço da passagem foi de R${:.2f}".format(dis*0.50))
else:
    print("O preço da passagem foi de R${:.2f}".format(dis*0.45))

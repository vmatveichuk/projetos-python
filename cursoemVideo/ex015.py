km = float(input('Digite a quantidade de km percorridos: '))
dias = float(input('Digite a quantidade de dias alugados: '))
preco = (dias * 60) + (km * 0.15)
print('O preço total foi de R${:.2f}'.format(preco))

from datetime import date
atual = date.today().year
s = 0
m = 0
for c in range(1, 8):
    nasc = int(input("Digite o ano de nascimento da {}° pessoa: ".format(c)))
    idade = atual - nasc
    if idade < 21:
        s += 1
    else:
        m += 1
print("Existem {} pessoa(s) maior(es) de idade".format(m))
print("Existem {} pessoa(s) menor(es) de idade".format(s))

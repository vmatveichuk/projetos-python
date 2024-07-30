from datetime import date
ano = int(input("Digite seu ano de nascimento: "))
atual = date.today().year
idade = atual - ano
if idade > 18:
    print("Já passou seu tempo de alistar, já se passaram {} ano(s) do seu alistamento".format(idade - 18))
elif idade == 18:
    print("É a hora de se alistar")
else:
    print("Ainda você vai se alistar, falta {} ano(s) para seu alistamento".format(18 - idade))

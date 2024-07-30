tupla = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
         "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
n = int(input("Digite um número entre 0 e 20: "))
while not n >= 0 or not n <= 20:
    n = int(input("Tente novamente. Digite um número entre 0 e 20: "))
print("Você digitou o número {}".format(tupla[n]))

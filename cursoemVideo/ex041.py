from datetime import date
ano = int(input("Digite seu ano de nascimento: "))
atual = date.today().year
idade = atual - ano

if idade <= 9:
    print("Categoria \33[1;31mMIRIM\33[m")
elif idade <=14:
    print("Categoria \33[1;32mINFANTIL\33[m")
elif idade <= 19:
    print("Categoria \33[1;33mJUNIOR\33[m")
elif idade <= 20:
    print("Categoria \33[1;34mSÊNIOR\33[m")
else:
    print("Categoria \33[1;35mMASTER\33[m")

s = str(input("Digite seu sexo: ")).upper().strip()[0]
while s not in "MF":
    s = str(input("Dados inválidos, digite seu sexo: ")).upper().strip()[0]
print("Sexo {} registrado com sucesso!".format(s))

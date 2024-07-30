comp1 = float(input("Digite o valor do primeiro comprimento de reta: "))
comp2 = float(input("Digite o valor do segundo comprimento de reta: "))
comp3 = float(input("Digite o valor do terceiro comprimento de reta: "))
if comp1 < comp2 + comp3 and comp2 < comp1 + comp3 and comp3 < comp1 + comp2:
    print("Os comprimentos de retas conseguem formar um triângulo")
else:
    print("Os comprimentos de reta não conseguem formar um triângulo")

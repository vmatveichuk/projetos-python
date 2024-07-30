comp1 = float(input("Digite o valor do primeiro comprimento de reta: "))
comp2 = float(input("Digite o valor do segundo comprimento de reta: "))
comp3 = float(input("Digite o valor do terceiro comprimento de reta: "))

if comp1 < comp2 + comp3 and comp2 < comp1 + comp3 and comp3 < comp1 + comp2:
    print("Os comprimentos de retas conseguem formar um triângulo")
    if comp1 != comp2 and comp1 != comp3 and comp2 != comp3:
        print("Este triângulo é \33[1;31mescaleno\33[m")
    elif comp1 == comp2 and comp1 == comp3 and comp2 == comp3:
        print("Este triângulo é \33[1;32mequilatero\33[m")
    else:
        print("Este triângulo é \33[1;34misósceles\33[m")

else:
    print("Os comprimentos de reta não conseguem formar um triângulo")

n = int(input("Digite o valor da tabuada: "))
print(10 * "\33[1;33m-=-\33[m")
print("\33[1;31mTABUADA DO {}\33[m".format(n))
for c in range(1, 11):
    m = n * c
    print("{} X {} = {}".format(n, c, m))
print(10 * "\33[1;33m-=-\33[m")
print("FIM")

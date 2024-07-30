p = int(input("Digite o 1° termo da PA: "))
r = int(input("Digite a razão: "))
d = p + (10 - 1) * r
for c in range(p, d + r, r):
    print(c, end=" -> ")
print("ACABOU")

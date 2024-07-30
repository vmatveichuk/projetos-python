p = int(input("Digite o 1° termo da PA: "))
r = int(input("Digite a razão: "))
termo = p
cont = 1
tot = 0
mais = 10
while mais != 0:
    tot += mais
    while cont <= tot:
        print("{} -> ".format(termo), end="")
        termo += r
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print("Progressão finalizada com {} termos mostrados".format(tot))
print("FIM")

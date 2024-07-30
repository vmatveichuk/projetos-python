ficha = list()
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input("Quer continuar: [S/N] ")).strip().upper()[0]
    if resp in "N":
        break
print("-=" * 30)
print(f"{'N°':<4}{'NOME':<10}{'MÉDIA':>8}")
print("-" * 26)
for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
while True:
    print("-" * 35)
    opcao = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if opcao == 999:
        break
    if opcao <= len(ficha) - 1:
        print(f"Notas de {ficha[opcao][0]} são {ficha[opcao][1]}")
print("<<< VOLTE SEMPRE >>>")

n1 = int(input("Digite o 1° valor: "))
n2 = int(input("Digite o 2° valor: "))

print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')

a = int(input("Digite a operação que você deseja: "))
while a != 5:
    if a == 1:
        print("A soma entre {} e {} é {}".format(n1, n2, n1 + n2))
        a = int(input("Digite a operação que você deseja: "))
    elif a == 2:
        print("O produto entre {} e {} é {}".format(n1, n2, n1 * n2))
        a = int(input("Digite a operação que você deseja: "))
    elif a == 3:
        if n1 > n2:
            print("O maior número é {}".format(n1))
            a = int(input("Digite a operação que você deseja: "))
        elif n1 < n2:
            print("O maior número é {}".format(n2))
            a = int(input("Digite a operação que você deseja: "))
        else:
            print("Não existe maior número, os dois números são iguais")
    elif a == 4:
        n1 = int(input("Digite um novo valor: "))
        n2 = int(input("Digite um outro novo valor: "))
        a = int(input("Digite a operação que você deseja: "))
    else:
        print("Você digitou nenhum dos valores possíveis")
        a = int(input("Digite a operação que você deseja: "))
print("Você saiu do programa")
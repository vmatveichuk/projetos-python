import random
cont = 0
pc = random.randint(0, 10)
while True:
    n = int(input("Digite um valor: "))
    opcao = str(input("Par ou Ímpar [P/I]: ")).upper().strip()[0]
    soma = pc + n
    if opcao == "P":
        if soma % 2 == 0:
            print("-----------------------------------------")
            print(f"Você jogou {n} e o computador jogou {pc}. Total de {soma} deu PAR")
            print("Você VENCEU!!!")
            print("Vamos jogar novamente...")
            cont += 1
        if soma % 2 != 0:
            print("-----------------------------------------")
            print(f"Você jogou {n} e o computador jogou {pc}. Total de {soma} deu IMPAR")
            print("Você perdeu")
            print(f"Game Over! Você venceu {cont} vezes")
            break
    if opcao == "I":
        if soma % 2 != 0:
            print("-----------------------------------------")
            print(f"Você jogou {n} e o computador jogou {pc}. Total de {soma} deu ÍMPAR")
            print("Você VENCEU!!!")
            print("Vamos jogar novamente...")
            cont += 1
        if soma % 2 == 0:
            print("-----------------------------------------")
            print(f"Você jogou {n} e o computador jogou {pc}. Total de {soma} deu PAR")
            print("Você perdeu")
            print(f"Game Over! Você venceu {cont} vezes")
            break

n = int(input("Digite um valor: "))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print("\33[31m", end=" ")
        tot += 1
    else:
        print("\33[33m", end=" ")
    print(c, end="")
print("\n \33[mO número {} foi divisível {} vezes".format(n, tot))
if tot == 2:
    print("E por isso ele é primo")
else:
    print("E por isso ele não é primo")


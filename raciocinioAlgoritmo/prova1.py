maior = list()
div = list()
impar = list()
soma = 0

while True:
    n = int(input("Digite um número: "))
    if n == -1:
        break
    if n > 30:
        maior.append(n)
    if n % 3 == 0:
        div.append(n)
    if n % 2 != 0:
        impar.append(n)
    if n % 2 == 0:
        soma += n

print("Maiores de 30:", maior)
print("Divisíveis por 3:", div)
print("Ímpares:", impar)
print("A soma dos pares:", soma)
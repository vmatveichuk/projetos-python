from random import shuffle
a1 = input('Qual é o primeiro aluno? ')
a2 = input('Qual é o segundo aluno? ')
a3 = input('Qual é o terceiro aluno? ')
a4 = input('Qual é o quarto aluno? ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação é')
print(lista)

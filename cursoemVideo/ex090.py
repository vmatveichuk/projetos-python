aluno = {}
aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input(f"Média de {aluno['nome']} : "))
situacao = ""
if aluno['media'] >= 7.0:
    situacao = "Aprovado"
elif aluno['media'] < 7.0 and aluno['media'] >= 4.0:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"
print(f"Nome é igual a {aluno['nome']}")
print(f"Média é igual a {aluno['media']}")
print(f"Situação é igual a {situacao}")

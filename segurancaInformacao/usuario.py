nome = "Victor"
u = "victor"
s = "12345"

print(20 * "=")
print("Entre com seu usuário")
print(20 * "=")
usuario = str(input("Digite seu login: ")).strip()
senha = str(input("Digite sua senha: "))

while usuario != u or senha != s:
    print("Login ou senha incorreta, tente novamente")
    usuario = str(input("Digite novamente seu login: "))
    senha = str(input("Digite novamente sua senha: "))

if usuario == u or senha == s:
    print("Bem vindo, {}".format(nome))
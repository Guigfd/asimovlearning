username = input("Qual o seu nome de usuário? ")
password = input("Qual a sua senha? ")

correct_password = "labrador"
correct_username = "admin"

if username == correct_username and password == correct_password:
    print(f"Bem vindo {username}")

elif username != correct_username:
    print("Nome de usuário incorreto")

elif password != correct_password and username == correct_username:
    print("Senha incorreta")

else:
    print("Senha e usuário incorretos")



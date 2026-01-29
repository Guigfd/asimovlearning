clientes = [
    ('Ana', 'xxx', '2'),
    ('john', 'xx2x', '5'),
    ('orfeu', 'x4x','12')
]


for cliente in clientes:
    nome, cpf, email = cliente # define as variaveis de acordo com as informacoes dentro da tupla
    print(f'Nome: {nome} - Cpf: {cpf} - Email: {email}')


secret_number = 10

for n in range (2):
    print(f'O valor de n é: {n}')

for tries in range (3):
    chute = int(input("Chute um número: "))
    if chute > secret_number:
        print("O seu número é maior que o número correto!")
    if chute < secret_number:
        print("O seu número é menor que o número correto!")
    if chute == secret_number:
        print("Correto!")
        break



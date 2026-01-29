# Programa que pede o nome e a idade:

name = input("Digite seu nome: ")
age = int(input("Digite sua idade: "))

print('-----')
print(f'Olá, {name}!')
print(f"Seu nome tem {len(name)} letras") # Se usar f no inicio do print e {} não é preciso converter usando str()
print(f"Depois de 5 anos sua idade será: {(age + 5)}")
print('-----')
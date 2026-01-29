age = int(input("Digite sua idade: "))

if age < 18:
    print("Você é menor de idade")

elif age == 18:
    print("Você tem 18 anos! Parabéns :)")

else:
    print("Você é maior de idade")


# ----------------------

# teste aula

print("------inicio------")

isHungry = input("Você está com fome? ")

if isHungry == "Sim":
    haveFood = input("Tem comida em casa? ")
    if haveFood == "Sim":
        print("Prepare uma refeição e pode comer!")
    else:
        print("Vá ao mercado!")
        print("Volte para casa!")
        print("Preparar a refeição")
        print("Comer a comida")



print("\n---------FIM------") # \n adiciona uma linha

# operadores booleanos

# and or not

estou_com_fome = input("Você está com fome? ") == "Sim"

if estou_com_fome:
    haveFood = input("Tem comida em casa? ") == "Sim"
    if haveFood:
        print("Prepare uma refeição e pode comer!")
    else:
        print("Vá ao mercado!")
        print("Volte para casa!")
        print("Preparar a refeição")
        print("Comer a comida")
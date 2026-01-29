
run_code = True
guesses = 0
correct_num = 128
total_guesses = 3

while run_code:

    guesses += 1

    if guesses <= total_guesses:
        num_input = input("Chute um numero inteiro: ")
        num = int(num_input)

        if num > correct_num:
            print("Seu número é MAIOR que o número correto!")

        elif num < correct_num:
            print("Seu número é MENOR que o número correto!")

        elif num == correct_num:
            print("Acertou!")
            break

    else:
        print("Você errou!")
        break



print("You are playing a number guessing game\n")

winning_number = int(input("Enter the winning number : "))                          # Input your winning number...

guessed_value = int(input("Maximum number of guesses you want to take ? "))         # Enter number of guesses ---> guessed_value

number_of_guesses = 1

input_number = int(input("Enter a number between 1 and 100 : "))                    # Here enter your desired number ---> input_number

game_over = False


while (not game_over and (number_of_guesses <= guessed_value)):                     # Here the condition check                           

    if (input_number == winning_number):
        print(f"You won the game in {number_of_guesses} times")
        game_over = True

    elif (input_number > winning_number):
        print(f"{guessed_value - number_of_guesses} left chances : Your number is too high : Guess low")
        input_number = int(input("Again enter a number "))
        number_of_guesses += 1

    elif (input_number < winning_number):
        print(f"{guessed_value - number_of_guesses} left chances : Your number is too low : Guess high")
        input_number = int(input("Again enter a number "))
        number_of_guesses += 1

if (number_of_guesses > guessed_value):                    # If your number of guesses exceeds the guessed_value then you lose the game ...
    print("\n\t\tYou lose the game")

print("You are playing a number guessing game\n")

winning_number = int(input("Enter the winning number : "))

game_value = int(input("Maximum number of guesses you want to take ? "))

guess = 1
input_num = int(input("Enter a number between 1 and 100 : "))

game_over = False

while (not game_over and (guess <= game_value)):

    if (input_num == winning_number):
        print(f"You won the game in {guess} times")
        game_over = True

    elif (input_num > winning_number):
        print(f"{game_value - guess} left chances : Your number is too high : Guess low")
        input_num = int(input("Again enter a number "))
        guess += 1

    elif (input_num < winning_number):
        print(f"{game_value - guess} left chances : Your number is too low : Guess high")
        input_num = int(input("Again enter a number "))
        guess += 1

if (guess > game_value):
    print("\n\t\tYou lose the game")

import random
end = False
print("Welcome to the Number Guessing Game!")
while not end:
    

    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)

    previous_guesses = []
    level = None

    def get_feedback(number, guess):
        difference = number - guess
        if difference > 0:
            if difference <= 5:
                return "slightly low"
            elif difference <= 15:
                return "low"
            elif difference <= 30:
                return "very low"
            elif difference <= 50:
                return "extremely low"
            else:
                return "way too low"
        else:
            if difference >= -5:
                return "slightly high"
            elif difference >= -15:
                return "high"
            elif difference >= -30:
                return "very high"
            elif difference >= -50:
                return "extremely high"
            else:
                return "way too high"

    # Choose the difficulty level
    difficulty = input("Press 'e' for Easy level or 'h' for Hard level: ").lower()

    if difficulty == "e":
        level = 10
    elif difficulty == "h":
        level = 5
    else:
        print("you are in trouble, it's way hard mode!")
        level = 2

        
    game_over = False

    # Main game loop
    while not game_over and level > 0:
        try:
            guess = int(input("Guess the number (between 1 and 100): "))

            if guess in previous_guesses:
                print(f"You already guessed {guess}. Try again!")
                continue

            previous_guesses.append(guess)

            if guess == random_number:
                print(f"Congratulations! You guessed the number {random_number} correctly!")
                game_over = True
            else:
                print(f"Your guess is {get_feedback(random_number, guess)}")
                level -= 1
                if level > 0:
                    print(f"You have {level} chances remaining.")
                else:
                    print(f"Game over! The correct number was {random_number}.")
                    game_over = True
        except ValueError:
            print("Invalid input. Please enter a number.")


    ask_for_end = input("press any key for continue the game or n for close")
    if ask_for_end == "n":
        end = True
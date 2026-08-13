import random
def main():
    print("Welcome to the Guessing The Number Game!")
    print("Difficulty Levels:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    users_choice=int(input("Choose a difficulty level (1-3): "))
    if users_choice==1:
        play_game(50)
    elif users_choice==2:
        play_game(100)
    elif users_choice==3:
        play_game(500)
    else:
        print("Enter the Valid level of Difficulty")   
        
def play_game(max_number):
    secret_number = random.randint(1, max_number)
    attempts = 0
    guess = None

    while guess != secret_number:
        attempts += 1
        guess = int(input(f"Guess a number (1-{max_number}): "))

        if guess == secret_number:
            print("You guessed it right!")
        elif guess > secret_number:
            print("Your guess is high. Try again.")
        else:
            print("Your guess is low. Try again.")

    print("You guessed the number in", attempts, "attempts.")
    print("Thank you for playing the guessing game!")
    
main()
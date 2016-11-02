import random

def intro():
    print("-----Welcome to the guessing game?-----")
    print("-----Its guessing time-----")
    play = ""
    while play != "Yes" or "No":
        play = input("Would you like to play the game? Please type Yes or No ")
        if play == "Yes":
            print("Let's Play")
            break
        elif play == "No":
            print("Goodbye")
            exit()
        else:
            print("What the heck did you type? Try again.")

def guess():
    guess = ""
    rando = random.randint(1, 10)
    while guess != rando:
        while True:
            try:
                guess = int(input('Please type your guess : '))
                break
            except ValueError:
                print("Sorry, this is not a number. Try again")
        if guess == rando:
            print("Great work man!")
        elif guess < rando:
            print('Your Guess was too high please type your next guess')
        elif guess > rando:
            print('Your Guess was too low please type your next guess')
        else:
            print("Are you sure you are doing this righ!")

def main():
    intro()
    guess()

main()

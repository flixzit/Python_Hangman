# Description: Hangman game
# made by: flixzit

import random

# List of words to choose from (add more if you want)
words = ['car', 'banana', 'house', 'nuts', 'fish', 'school', 'mines', ]

# Choose a random word
randomword = random.choice(words)

# The number of turns the player has
max_turns = 7

# The letters will be stored in this list
guesses = []


# Print the blank spaces for the word
def print_randomword():
    for letter in randomword:
        if letter in guesses:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print()


# Start the game
def start_game():
    # Keep playing until the player wins or loses
    print('Welcome to Hangman! The word has', len(randomword), 'letters try to guess it.')
    turns = 0
    while turns < max_turns:
        print_randomword()
        print('Guess a letter: ')

        # Print the number of turns left
        print('Turns left:', max_turns - turns)


        guess = input().lower()

        # If the letter has already been guessed, tell the player and continue
        if guess in guesses:
            print('You already guessed that letter!')
            continue


        #check if the input is a letter

        if guess.isalpha() == False:
            print("please enter a letter")
            continue

        # Add the letter to the list of guesses
        guesses.append(guess)

        # If the letter is in the word, tell the player
        if guess in randomword:
            print('Good guess!')
        else:
            print('Sorry, that letter is not in the word.')
            turns += 1

        # If the player has guessed all the letters, they win
        if all(letter in guesses for letter in randomword):
            print_randomword()
            print('You win!')
            return

        # If the player has run out of turns, they lose
        if turns == max_turns:
            print('You lost! The word was', randomword)
            (print("------------------"))
            print("want to play again? (y/n)")
            answer = input()

            if answer == "y":
                start_game()
            else:
                print("Thanks for playing Hangman!")
            return

#Starts the game
start_game()
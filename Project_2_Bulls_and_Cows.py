# head
line = "-" * 60
print(line)
print("project_2.py: Druhý projekt do Engeto Online Python Akademie")
print("\nautor: Lucie Anděrová")
print("e-mail: anderova.l@email.cz")
print("discord: luciea._14885")
print(line)

import random
import time

total_games = 0
total_guesses = 0
total_time = 0


def welcome_player():
    """
    Asks name of the player, welcomes the player.
    """
    name = input("Hello, what's your name? ")
    print(f"Welcome, {name}, let's play bulls and cows game!")
    print("I have generated a random 4 digit number. ")
    print(line)


def generate_unique_4_digit_number():
    """
    Generates random unique number, returns random number.
    """
    while True:
        random_number = random.randint(1000, 9999)
        digits = [int(digit) for digit in str(random_number)]
        if len(set(digits)) == 4:
            return str(random_number)


def get_user_guess():
    """
    Asks for user guess, verifies if it is a 4-digit number.
    """
    while True:
        guess = input("Enter your guess (4-digit number with unique digits): ")
        if guess.isdigit() and len(guess) == 4 and len(set(guess)) == 4 and not guess.startswith("0"):
            return guess
        else:
            print("Invalid input. Please enter a 4-digit number with unique digits that doesn't start with 0.")


def compare_guess_and_random_number(guess, number):
    """
    Compares user guess and random number, counts bulls and cows.
    """
    bulls = 0
    cows = 0

    for i in range(len(guess)):
        if guess[i] == number[i]:
            bulls += 1
        elif guess[i] in number:
            cows += 1
    return bulls, cows


def play_game():
    """
    Allows user to play the game, counts guesses, games and time.
    """
    global total_guesses, total_games, total_time
    total_games += 1
    guesses = 0
    start_time = time.time()
    random_unique_number = generate_unique_4_digit_number()

    while True:
        user_guess = get_user_guess()
        bulls, cows = compare_guess_and_random_number(user_guess, random_unique_number)
        guesses += 1
        print(f"You have {bulls} {'bull' if bulls == 1 else 'bulls'} and {cows} {'cow' if cows == 1 else 'cows'}.")

        if bulls == 4:
            end_time = time.time()
            game_time = end_time - start_time
            print(
                f"Congratulations! You guessed the correct number in {guesses} "
                f"{'guess' if guesses == 1 else 'guesses'}.")
            print(f"Game time: {game_time:.2f} seconds.")
            total_guesses += guesses
            total_time += game_time
            break
    play_again = input("Do you want to play again? (yes/no): ")
    return play_again.lower() == 'yes'


def main():
    """
    Lets user play the game, counts games, average guesses and average time.
    """
    global total_games, total_guesses, total_time
    welcome_player()

    while True:
        if not play_game():
            break

    print(f"Total games played: {total_games}")
    if total_games > 0:
        average_guesses = total_guesses / total_games
        average_time = total_time / total_games
        print(f"Average guesses per game: {average_guesses:.2f}.")
        print(f"Average time per game: {average_time:.2f} seconds.")


main()

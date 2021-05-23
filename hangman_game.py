#!/usr/bin/env python
# coding: utf-8

import random
from collections import defaultdict
import graphics


def encode_secret(secret):
    """encode secret to hex values"""
    return "".join(["{:02x}".format(ord(item)) for item in secret])


def decode_secret(secret_hex):
    """decode secret hex"""
    return bytearray.fromhex(secret_hex).decode()


class HangmanGame:
    """hangman game class"""

    def __init__(self):
        self.name = ""
        self.players_score = defaultdict(int)
        self.exit_game_status = False
        self.encoded_secrets = [
            "53656e73796e65204865616c7468",
            "4d616368696e65204c6561726e696e67",
            "436c696e6963616c6c792064726976656e",
            "4461746120456e67696e656572696e67",
        ]

    def help_section(self):
        """help section"""
        print("\n[HELP]")
        print(
            """
Playing Hangman
Hangman is an old school favorite, a word game where the goal is simply to find the missing word or words.
You will be presented with a number of blank spaces representing the missing letters you need to find.
Use the keyboard to guess a letter (I recommend starting with vowels).
If your chosen letter exists in the answer, then all places in the answer where that letter appear will be revealed.
After you've revealed several letters, you may be able to guess what the answer is and fill in the remaining letters.
Be warned, every time you guess a letter wrong you loose a life and the hangman begins to appear, piece by piece.
The player gets 5 letter guesses before losing the game. The game is lost on the 6th bad guess.
Every time a player wins the game, they get 10 points.
Good Luck !
        """
        )

    def exit_game(self):
        """exit game"""
        print("\n[EXIT]")
        self.exit_game_status = True

    def about(self):
        """about the author"""
        print("\n[ABOUT]")
        print("Hangman Game")
        print("Seb Slisz")
        print("Gloucester, UK")
        print("2021")
        print()

    def update_score(self):
        """update players score"""
        self.players_score[self.name] += 10

    def show_leaderboard(self):
        """show leaderboard section"""
        print("\n[LEADERBOARD SECTION]")
        sorted_ranking = sorted(
            list(self.players_score.items()), key=lambda x: x[1], reverse=True
        )
        sorted_ranking = sorted_ranking[:10]  # only top 10
        for index, (key, value) in enumerate(sorted_ranking):
            print("{}. {} {}".format(index + 1, key, value))
        print()

    def main_menu(self):
        """main menu"""
        while True:
            print("\n[MAIN MENU]")
            print("1. NewGame")
            print("2. Leaderboard")
            print("3. Help")
            print("4. About")
            print("5. Exit")
            print()

            while True:
                choice = input("Enter a choice and press enter: ")
                if choice == "1":
                    self.initialise_game()
                elif choice == "2":
                    self.show_leaderboard()
                elif choice == "3":
                    self.help_section()
                elif choice == "4":
                    self.about()
                elif choice == "5":
                    self.exit_game()
                else:
                    print("Type number between 1-5")
                    continue
                break

            if self.exit_game_status:
                break
            input("Press enter to go back to the main menu ")

    def initialise_game(self):
        """initialise game"""
        print("\n[NEW GAME]")
        self.name = input("What is your name? ")
        self.players_score[self.name]

        # Here the user is asked to enter the name
        print("Good Luck {}!".format(self.name))
        word = decode_secret(random.choice(self.encoded_secrets))
        guesses = ""
        fails = 0

        while True:
            # all characters from the input word taking one at a time
            updated_secret = ""
            for char in word:
                # comparing that character with the character in guesses
                if char in guesses:
                    updated_secret += char
                else:
                    updated_secret += "_"
            print(updated_secret)

            if updated_secret == word:
                # perform winning the game
                print("You win!\nThe word is: {}".format(word))
                self.update_score()
                self.show_leaderboard()
                break

            # ask user to type character
            guess = input("Guess a character: ")
            guesses += guess

            if guess == "":
                continue

            if len(guess) > 1:
                print("Type only one character")
                continue

            # check input with the character in word
            if guess in word:
                print("Correct!\n")
            else:
                # if the character doesn’t match the word
                # then “Wrong” will be given as output
                fails += 1
                print("Wrong. FailsCount: {}\n".format(fails))
                graphics.update_status(fails - 1)

                if fails > 5:
                    print("You Loose")
                    self.show_leaderboard()
                    break


if __name__ == "__main__":
    game = HangmanGame()
    game.main_menu()

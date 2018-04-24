# Command Line Hangman
# Two Player local
# Created when refreshing my python

import os
import time


class Hangman:
    """Creates and runs Hangman game"""
    STATES = \
        [
            '   ______\n'
            '   |     |\n'
            '   |\n'
            '   |\n'
            '   |\n'
            '   |\n'
            '___|___\n'
            '\nYou have 6 lives remaining',
            '   ______\n'
            '   |     |\n'
            '   |    [_]\n'
            '   |\n'
            '   |\n'
            '   |\n'
            '___|___\n'
            '\nYou have 5 lives remaining',
            '   ______\n'
            '   |     |\n'
            '   |    [_]\n'
            '   |     |\n'
            '   |     |\n'
            '   |\n'
            '___|___\n'
            '\nYou have 4 lives remaining',
            '   ______\n'
            '   |     |\n'
            '   |    [_]\n'
            '   |   __|\n'
            '   |     |\n'
            '   |\n'
            '___|___\n'
            '\nYou have 3 lives remaining',
            '   ______\n'
            '   |     |\n'
            '   |    [_]\n'
            '   |   __|__\n'
            '   |     |\n'
            '   |\n'
            '___|___\n'
            '\nYou have 2 lives remaining',
            '   ______\n'
            '   |     |\n'
            '   |    [_]\n'
            '   |   __|__\n'
            '   |     |\n'
            '   |   _/\n'
            '___|___\n'
            '\nYou have 1 life remaining',
            '   ______\n'
            '   |     |\n'
            '   |    [_]\n'
            '   |   __|__\n'
            '   |     |\n'
            '   |   _/ \_\n'
            '___|___\n'
            '\nGame Over.\nYou have been hanged!\nPlayer One wins!'
        ]
    state = 0
    game_over = False
    guessed_letters = []

    def __init__(self):
        """Initializes and runs game"""

        # Game setup
        word = raw_input('Player One, enter a word:\n')
        self.answer = [c.lower() for c in word]
        self.hidden_answer = []
        for x in self.answer:
            if x == ' ':
                self.hidden_answer += ' '
            else:
                self.hidden_answer += '_'
        os.system('clear')
        print 'Game starting...'
        time.sleep(1)
        print 'Player two step up.'
        time.sleep(1)

        # Main game loop
        while not self.game_over:
            self.update_graphic()
            guess = self.get_valid_input()
            self.check_answer(guess)

        # Game has finished; check winner and print result
        if self.state == 6:
            print '{} The answer was {}.'.format(self.STATES[6], ''.join(self.answer))
        else:
            print 'Game Over.\nThe answer was {}.\nPlayer Two wins!'.format(''.join(self.answer))

    def update_graphic(self):
        """Print game state"""
        os.system('clear')
        print 'Guessed letters: {}'.format(self.guessed_letters)
        print ' '.join(self.hidden_answer)
        print self.STATES[self.state]

    def get_valid_input(self):
        """Prompts for input for guess and validates it

        Returns:
            char: A valid letter entered by player
        """
        valid = False
        while not valid:
            given = raw_input('Guess a letter:\n')
            if len(given) == 1 and given.isalpha() and given.lower() not in self.guessed_letters:
                valid = True
            else:
                print 'Input must be a single letter which has not already been guessed. Try again.'

        return given.lower()

    def check_answer(self, guess):
        """Checks if answer contains guessed letter and update game states

        Args:
            guess(char): Validated letter which has been entered
        """
        self.guessed_letters.append(guess)
        correct = False
        for index, letter in enumerate(self.answer):
            if letter == guess:
                correct = True
                self.hidden_answer[index] = guess

        if not correct:
            # Adds body part to ascii art
            self.state += 1
            if self.state == 6:
                self.game_over = True
        elif self.hidden_answer == self.answer:
            # Entire answer revealed
            self.game_over = True


# Creates game object with run from command line
Hangman()

"""
Program: words_lists
Author: Jacob Sharpe
Last date modified: 7/31/2020

this program holds all of the game mechanics of the hangman program that the GUI calls to
to display
"""
import random
import array as arr
from classes.words_lists import create_lists


class mechanics():
    def __init__(self):
        self.cl = create_lists()
        self.game_started = False
        self.game_difficulty = ""
        self.game_word = ""
        self.game_word_list = []
        self.word_length = -1
        self.word_output_list = arr.array('b', [])
        self.tries = -1
        self.letters_guessed = []
        self.right_answers = 0
        self.win_lose_playing = ""
        self.number_of_wins = 0
        self.number_of_losses = 0
        self.word_attempted = False
        self.word_completed = False

    def start_new_game(self, game_state, difficulty):
        """this function clears the current game's info and calls to other functions to
        set up a new game
        if the game has been started and a new game is started without finishing
        then it will increase the number of losses by one
        :param game_state, is true if the game is being played, false if not
        :param difficulty, sets the difficulty of the game
        """
        if self.word_attempted == True and self.word_completed == False:
            self.number_of_losses += 1
        self.word_attempted = False
        self.word_completed = False
        self.game_difficulty = ""
        self.game_word = ""
        self.game_word_list = []
        self.word_length = -1
        self.word_output_list = []
        self.tries = -1
        self.letters_guessed = []
        self.right_answers = 0

        self.win_lose_playing = "Playing"
        self.set_game_started(game_state)
        self.set_game_difficulty(difficulty)
        self.set_new_word()
        self.set_tries()

    def set_game_started(self, game_state):
        """ sets whether the game has started or not
        :param game_state, true if the game is to be played, false if not
        """
        self.game_started = game_state

    def get_game_started(self):
        """ returns the game started value
        :return game_started
        """
        return self.game_started

    def set_game_difficulty(self, difficulty):
        """ sets the game difficulty
        :param difficulty
        """
        self.game_difficulty = difficulty

    def get_game_difficulty(self):
        """ returns the game difficulty
        :return game_difficulty
        """
        return self.game_difficulty

    def set_new_word(self):
        """ determines what word is to be used this session based in the difficulty
        also determines the word's length and puts the game word in a list as well as
        create the hidden word list
         """
        try:
            if self.game_difficulty == "Easy":
                self.word_list_to_use = self.cl.create_easy_list()
            elif self.game_difficulty == "Medium":
                self.word_list_to_use = self.cl.create_medium_list()
            elif self.game_difficulty == "Hard":
                self.word_list_to_use = self.cl.create_hard_list()

            self.game_word = random.choice(self.word_list_to_use)
            self.game_word_list[:0] = self.game_word
            self.word_length = len(self.game_word)
            self.word_output_list[:0] = "_" * self.word_length
        except:
            self.game_started = False

    def get_word_length(self):
        """ returns the game word length
        :return word_length
        """
        return self.word_length

    def set_tries(self):
        """ sets the number of tries determined by the difficulty
        """
        if self.game_difficulty == "Easy":
            self.tries = 10
        elif self.game_difficulty == "Medium":
            self.tries = 8
        elif self.game_difficulty == "Hard":
            self.tries = 6

    def get_tries(self):
        """ returns the number of tries
        :return tries
        """
        return self.tries

    def display_game_word_results(self):
        """ returns the word with the right letters guessed
        :return result the parts of the word that has been guessed right
        """
        result = ""
        for x in self.word_output_list:
            result = result + x + " "
        return result

    def guess(self, letter_answer):
        """ main portion
        determines if a letter has been already guessed and
        also sees if the letter guessed is a correct letter in the word
        also determines if the entire word has been guessed or if there
        are no more tries left
        :param letter_answer, the letter that has been guessed
        """
        self.word_attempted = True
        correct_answer = False
        letter_already_guessed = False
        for x in range(len(self.letters_guessed)):
            if self.letters_guessed[x] == letter_answer:
                letter_already_guessed = True

        if letter_already_guessed == False:
            for x in range(len(self.game_word_list)):
                if self.game_word_list[x] == letter_answer:
                    self.word_output_list[x] = letter_answer
                    self.letters_guessed.append(letter_answer)
                    self.right_answers += 1
                    correct_answer = True

        if correct_answer == False:
            self.tries -= 1

        if self.tries == 0:
            self.win_lose_playing = "Lose"
            self.number_of_losses += 1
            self.word_completed = True
        elif self.right_answers == self.word_length:
            self.win_lose_playing = "Win"
            self.number_of_wins += 1
            self.word_completed = True

    def return_win_or_lose(self):
        """ returns the state of the game
        :return win_lose_playing, returns if the game is won, lost or if it is still being played
         """
        return self.win_lose_playing

    def return_wins(self):
        """ returns the number of wins
        :return number_of_wins, returns how many times won
        """
        return self.number_of_wins

    def return_losses(self):
        """ returns the number of losses
        :return number_of_losses, returns how many times loss
        """
        return self.number_of_losses

    def display_game_word_loss_results(self):
        """ returns the full unhidden word if the game is lost
        :return result, the unhidden word if game is lost
        """
        result = ""
        for x in self.game_word_list:
            result = result + x + " "
        return result

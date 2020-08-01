"""
Program: words_lists
Author: Jacob Sharpe
Last date modified: 7/31/2020

the purpose of this program is to draw from a txt file the words and create seperate lists
that depend on the difficulty the palyer selected
"""
import re


class create_lists():
    def __init__(self):
        self.index = '../classes/words.txt'
        self.backup_index = 'words.txt' #use if the first index doesn't work

    def create_easy_list(self):
        """creates the easy list and return it if the txt file is present
        :return word_list, the word list
        """
        wrong_characters = set("-")
        self.word_list = []
        try:
            f = open(self.index, 'r')
            for line in f:
                if line[0] == 'E' and line[1] == " " and line[2] != " ":
                    readout = line[2:].upper()
                    has_digit = re.search('\d', readout)
                    # this can be added to if there are more characters that cannot be
                    #used in the game
                    has_wrong = re.search("[-,.' '/!?]", readout)
                    if has_digit is None:
                        if has_wrong is None:
                            self.word_list.append(readout.strip('\n'))
            return self.word_list
        except IOError:
            print("Cannot open file")
            raise (IOError)

    def create_medium_list(self):
        """creates the medium list and return it if the txt file is present
        :return word_list, the word list
        """
        word_list = []
        try:
            f = open(self.index, 'r')
            for line in f:
                if line[0] == 'M' and line[1] == " " and line[2] != " ":
                    readout = line[2:].upper()
                    has_digit = re.search('\d', readout)
                    # this can be added to if there are more characters that cannot be
                    # used in the game
                    has_wrong = re.search("[-,.' '/!?]", readout)
                    if has_digit is None:
                        if has_wrong is None:
                            word_list.append(readout.strip('\n'))
            return word_list
        except IOError:
            print("Cannot open file")
            raise (IOError)

    def create_hard_list(self):
        """creates the Hard list and return it if the txt file is present
        :return word_list, the word list
        """
        word_list = []
        try:
            f = open(self.index, 'r')
            for line in f:
                if line[0] == 'H' and line[1] == " " and line[2] != " ":
                    readout = line[2:].upper()
                    has_digit = re.search('\d', readout)
                    # this can be added to if there are more characters that cannot be
                    # used in the game
                    has_wrong = re.search("[-,.' '/!?]", readout)
                    if has_digit is None:
                        if has_wrong is None:
                            word_list.append(readout.strip('\n'))
            return word_list
        except IOError:
            print("Cannot open file")
            raise (IOError)

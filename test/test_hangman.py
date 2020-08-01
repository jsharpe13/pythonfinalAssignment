import unittest
from classes.words_lists import create_lists
from classes.game_mechanics import mechanics


class HangmanClassTest(unittest.TestCase):
    def setUp(self):
        self.cl = create_lists()
        self.gm = mechanics()

    def tearDown(self):
        del self.cl
        del self.gm

    def test_IO_validation(self):
        easy_list = self.cl.create_easy_list()
        not_valid_answer = 'mal3l'
        all_valid_answers = True
        for x in easy_list:
            if x == not_valid_answer:
                all_valid_answers = False
        self.assertTrue(all_valid_answers)

    def test_IO_Exception(self):
        with self.assertRaises(IOError):
            cl2 = create_lists()
            cl2.index = "words2.txt"
            easy_list = cl2.create_easy_list()

    def test_new_game_wins_the_same(self):
        self.gm.number_of_wins = 3
        self.gm.start_new_game(True, "Hard")
        self.assertEqual(self.gm.number_of_wins, 3)

    def test_new_game_losses_the_same(self):
        self.gm.number_of_losses = 4
        self.gm.start_new_game(True, "Hard")
        self.assertEqual(self.gm.number_of_losses, 4)

    def test_attempt_but_not_completed(self):
        self.gm.word_attempted = True
        self.gm.word_completed = False
        self.gm.start_new_game(True, "Hard")
        self.assertEqual(self.gm.number_of_losses, 1)

    def test_game_difficulty(self):
        self.gm.start_new_game(True, "Easy")
        self.assertEquals(self.gm.game_difficulty, "Easy")

    def test_easy_tries(self):
        self.gm.start_new_game(True, "Easy")
        self.assertEquals(self.gm.tries, 10)

    def test_medium_tries(self):
        self.gm.start_new_game(True, "Medium")
        self.assertEquals(self.gm.tries, 8)

    def test_hard_tries(self):
        self.gm.start_new_game(True, "Hard")
        self.assertEquals(self.gm.tries, 6)

    def test_length(self):
        self.gm.start_new_game(True, "Hard")
        self.assertEquals(len(self.gm.word_output_list), len(self.gm.game_word_list))
        self.assertEquals(len(self.gm.game_word), self.gm.word_length)

    def test_lost_display_word(self):
        self.gm.start_new_game(True, "Hard")
        word = " ".join(self.gm.game_word) + " "
        word2 = self.gm.display_game_word_loss_results()
        self.assertEquals(word2, word)

    def test_lost_game(self):
        self.gm.start_new_game(True, "Medium")
        self.assertEquals(self.gm.win_lose_playing, "Playing")


if __name__ == '__main__':
    unittest.main()

import unittest
from guess_game import GuessGame

class TestGuessGame(unittest.TestCase):
    def setUp(self):
        self.game = GuessGame()
        self.game.target = 50  # Fixed value for testing

    def test_guess_too_low(self):
        self.assertEqual(self.game.guess(25), "Too low!")

    def test_guess_too_high(self):
        self.assertEqual(self.game.guess(75), "Too high!")

    def test_guess_correct(self):
        self.assertEqual(self.game.guess(50), "Correct!")

    def test_guess_out_of_bounds(self):
        self.assertEqual(self.game.guess(0), "Out of bounds!")

if __name__ == '__main__':
    unittest.main()

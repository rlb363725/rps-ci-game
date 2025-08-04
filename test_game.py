# test_game.py
import unittest
from game import determine_winner

class TestRPSGame(unittest.TestCase):
    def test_tie(self):
        self.assertEqual(determine_winner("rock", "rock"), "Tie")

    def test_rock_beats_scissors(self):
        self.assertEqual(determine_winner("rock", "scissors"), "Player 1 wins")

    def test_scissors_beats_paper(self):
        self.assertEqual(determine_winner("scissors", "paper"), "Player 1 wins")

    def test_paper_beats_rock(self):
        self.assertEqual(determine_winner("paper", "rock"), "Player 1 wins")

    def test_invalid_input(self):
        self.assertEqual(determine_winner("rock", "lizard"), "Invalid input")

if __name__ == "__main__":
    unittest.main()

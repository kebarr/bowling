import unittest
import bowling

class PythonBowlingGame(unittest.TestCase):
    # initialise game in setup, exit in tear town
    def setup(self):
        self.game = Game(1)

    def test_gutter_game(self):
        roll_many(20, 0)
        assertEquals(0, self.game.score())

    def test_all_ones(self):
        roll_many(20, 1)
        assertEquals(20, self.game.score())

    def test_one_spare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        roll_many(17,0)
        assertEquals(16, self.game.score)

    def roll_many(self, n, pins)
        for i in range(n):
            self.game.roll(pins)


if __name__ == '__main__':
    unittest.main()

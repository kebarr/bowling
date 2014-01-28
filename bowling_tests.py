import unittest
from bowling import Game
import unittest

class PythonBowlingGame(unittest.TestCase):
    # initialise game in setup, exit in tear town
    def setUp(self): # oh dear all this over a capital U
        self.game = Game(1)
        #print "SETTING UP!!!"

    def test_gutter_game(self):
        #self.game = Game(1) # ok works here, why not in setup!?!?!?
        self.roll_many(20, 0)
        self.assertEqual(0, self.game.score()[0])

    def test_all_ones(self):
        self.roll_many(20, 1)
        self.assertEqual(20, self.game.score()[0])

    def test_one_spare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.roll_many(17,0)
        self.assertEqual(16, self.game.score()[0])

    # not sure if i'm supposed to include ALL tests to start off...
    def test_one_strike(self):
        self.game.roll(10)
        self.game.roll(3)
        self.game.roll(4)
        self.roll_many(16, 0)
        self.assertEqual(24, self.game.score()[0])

    def test_perfect_game(self):
        self.roll_many(12,10)
        self.assertEqual(300, self.game.score()[0])

    # may also be worth testing that the maximum number of rolls on last turn is 3

    def roll_many(self, n, pins):
        for i in range(n):
            self.game.roll(pins)


if __name__ == '__main__':
    unittest.main()

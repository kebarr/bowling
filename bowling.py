class Game:
    def __init__(self, players):
        # assume arbitrary number of players
        self.players = players
        self.scores = [0 for i in range(players)]
        # also need to store whether last roll was a spare or a strike
        self._spare = [False for i in range(players)]
        self._strike = [False for i in range(players)]
        # [1st, 2nd, bonus]
        self.frames = [[[None, None, None] for j in range(10)] for i in range(players)]
        self.running_total = [0 for i in range(players)]
        self.player = 0
        self.turn = 0


    def roll(self, pins):
        # to pss first test, don't really need to do anything.
        self.running_total[0] += pins
        return self.running_total

    def score(self, player=0):
        # exception if we've not finished the game?
        return self.running_total[player]

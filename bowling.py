class Game:
    def __init__(self, players):
        # assume arbitrary number of players
        self.players = players
        self.scores = [0 for i in range(players)] # is this actually used?
        # also need to store whether last roll was a spare or a strike
        self._spare = [False for i in range(players)]
        self._strike = [False for i in range(players)]
        # [1st, 2nd, bonus]
        self.frames = [[[None, None, None] for j in range(10)] for i in range(players)]
        self.running_total = [0 for i in range(players)]
        self.player = 0
        self.turn = 0
        
    # can move a lot of this functionality into score but couldn't show a running total that way
    # or, not really even sure why we need a score function, keep tabs of it here
    # this needs to know whether its the first or second roll, and which go were on
    # not really sure what a function which only takes pins would do. 
    # can store which player we're on as a variable and keep tabs of it in here. would need to do the same for roll
    def roll(self, pins):
        player = self.player
        turn = self.turn
        next_player = None
        if self.frames[player][turn][0] is None:
            # on first roll, 
            next_player = self.first_roll(pins, player, turn)
            if self._spare[player] == True:
                self.score_spare(pins, player, turn)
        else:
            if self._strike[player] == True:
                self.score_strike(pins, player, turn)
            total = self.second_roll(pins, player, turn)
            self.increment_player()
            self.turn = 0
        # increment turn if its not a strike, and not the second roll, so total has been defined
        elif total:
            self.turn = 1
        print self.running_total
        return self.running_total
    
    def increment_player(self):
        if self.player < self.players -1:
            self.player += 1
        elif self.player == self.players -1:
            # we're onto the next round
            self.player = 0
        else:
            print "Exceeded number of players!!"
            
    def first_roll(self, pins, player, turn):
        self.frames[player][turn][0] = pins
        if pins == 10:
                self._strike[player] = True
        return self._strike[player]
    
    def second_roll(self, pins, player, turn):
        self.frames[player][turn][1] = pins
    # if we make the second roll, its definitely not a strike!
        self._strike[player] == False
        if self.frames[player][turn][0] + self.frames[player][turn][1] == 10:
            self._spare[player] == True
        # if its neither a strike nor a spare, we can update the running total
        else:
            self.running_total[player] += self.frames[player][turn][0] + self.frames[player][turn][1]
        return self.running_total
    
    def score_strike(self, pins, player, turn):
        self.frames[player][turn-1][2] += pins
        self.running_total[player]+= self.frames[player][turn-1][0] + self.frames[player][turn-1][1] + self.frames[player][turn-1][2]

    def score_spare(self, pins, player, turn):
# previous frame has score from first roll added
        self.frames[player][turn-1][2] = pins
        # update running total
        self.running_total[player]+= self.frames[player][turn-1][0] + self.frames[player][turn-1][1] + self.frames[player][turn-1][2]
        # reset to False until score for this turn is calculated
        self._spare[player] = False

    def score(self):
        # exception if we've not finished the game?
        return self.running_total
            

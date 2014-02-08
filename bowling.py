class Game:
    def __init__(self, players):
        # assume arbitrary number of players
        self.players = players
        self.scores = [0 for i in range(players)] # is this actually used?
        # also need to store whether last roll was a spare or a strike
        self._spare = [False for i in range(players)]
        self._strike = [[False,0] for i in range(players)] # second number stores number of previous strikes
        # [1st, 2nd, bonus]
        self.frames = [[[None, None, None] for j in range(10)] for i in range(players)]
        self.running_total = [0 for i in range(players)]
        self.player = 0
        # turn is which of the 1 to 10 goes were on
        # not which or first or second roll
        self.turn = 0
        self.can_roll = [True for i in range(players)]
        self.last_turn_third_roll = [False for i in range(players)]

    def roll(self, pins):
        if pins > 10:
            return "cannot hit more than 10 pins"
        # special case for last roll
        if self.last_turn_third_roll[self.player]: # can only be this on last roll
            self.frames[self.player][9][2] = pins
            self.score_strike()
            #self.running_total[self.player] += 20 + pins
            print "last roll"
        else:
            self.standard_roll(pins)
            print "standard roll"
        return self.running_total

    def standard_roll(self, pins):
        player = self.player
        turn = self.turn
        if self.frames[player][turn][0] is None:
            # on first roll, so roll, then score if we had a spare
            self.first_roll(pins, player)
            if self._spare[player] == True:
                self.score_spare(pins, player, turn)
        else:
            # and whether we can roll, i.e. not a strike this turn.
            # update turn in second_roll if not a strike.
            if self.can_roll[player]:
                self.second_roll(pins, player, turn)            
            self.increment_player()

    
    def increment_player(self):
        self.can_roll[self.player] = True # this wont make all players able to- 
        if self.player < self.players -1:
            self.player += 1
        elif self.player == self.players -1:
            # we're onto the next round
            self.player = 0
            if self.turn < 9:
                self.turn += 1
                print "turn"
        else:
            print "Exceeded number of players!!"
            
    def first_roll(self, pins, player):
        turn = self.turn
        self.frames[player][self.turn][0] = pins
        if pins == 10:
                print "strike"
                if self.players > 1:
                    if turn != 9:
                        self.can_roll[player] = False
                elif turn != 9:
                    self.turn += 1 # only 1 player so increment turn on strike
                self._strike[player][0]= True
                self._strike[player][1] += 1
    
    def second_roll(self, pins, player, turn):
        print self.running_total, "second roll"
        self.frames[player][turn][1] = pins
        # if we make the second roll, its definitely not a strike!
        #self._strike[player] == False
        if self.frames[player][turn][0] + self.frames[player][turn][1] == 10:
            self._spare[player] = True
        # if its neither a strike nor a spare, we can update the running total
        else:
            if turn < 9 or pins < 10:
                #if turn != 9: don't want to increment running total if last turn and 10 pins
                self.running_total[player] += self.frames[player][turn][0] + self.frames[player][turn][1]
                # call score strike regardless of wheher its a strike or not, and deal with that there
                self.score_strike()
        #print self.running_total, "second roll 2"
        if turn == 9 and pins == 10:
            self.last_turn_third_roll[player] = True
            print "true"

    def score_strike(self):
        player = self.player
        turn = self.turn
        self._strike[player][0] = False
        # total each preceeding strike
        for i in range(self._strike[player][1]):
            print i
            # first will always be 2 in a row
            # test if there was a second throw on this turn
            if self.frames[player][turn-i][1] is not None:
                self.frames[player][turn-1 - i][2] = int(self.frames[player][turn - i][0] or 0) + int(self.frames[player][turn -i][1] or 0)
                self.running_total[player]+= int(self.frames[player][turn-1-i][0] or 0) + int(self.frames[player][turn-1-i][2] or 0)
                print "score next go"
            else:
                self.frames[player][turn-2-i][2] = self.frames[player][turn-1-i][0] + self.frames[player][turn-i][0]
                self.running_total[player] += self.frames[player][turn-2-i][0] + self.frames[player][turn-2-i][2] # no middle go
                print "two strikes"
        self._strike[player][1] = 0
        print self.running_total, "strike"

    def score_spare(self, pins, player, turn):
        #print "spare"
# previous frame has score from first roll added
        self.frames[player][turn-1][2] = pins
        # update running total
        self.running_total[player]+= self.frames[player][turn-1][0] + int(self.frames[player][turn-1][1] or 0) + int(self.frames[player][turn-1][2] or 0)
        # reset to False until score for this turn is calculated
        self._spare[player] = False

    def score(self):
        return self.running_total
            

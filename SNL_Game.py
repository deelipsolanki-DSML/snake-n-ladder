import random


class Board:
    def __init__(self, board_dictionary: dict):
        self.dic = board_dictionary


class Dice:
    def roll(self):
        n = random.randint(1,6)
        return n


class Player:
    def __init__(self, name):
        self.name = name  # string name
        self.status = -1  # lock : -1, complete: 1, inGame: 0
        self.rank = 0  # not ranked yet
        self.pos = -1  # { 1,2...100}  # -1 -> not started yet (start at first 6 appear on roll)
        self.dice = Dice()
    def move(self, number):
        self.pos += number

    def play(self):
        roll = self.dice.roll()

        if (self.status == -1):  # player is locked
            if roll == 6:
                print(f"Unlocked : {self.name} !")
                self.status = 0  # welcome to the game
                self.pos = 1
            else:
                print(f"{self.name} is Locked, Get no 6 to unlock")

        elif self.status == 0:  # in game
            self.move(roll)

        else:
            pass  # player has completed the game

# Ask for the no of players and board dictionary to create a game

class Game:
    def __init__(self, no_of_players, board_dictionary):
        self.nplayers = no_of_players
        self.board = Board(board_dictionary)
        self.game_status = 0  # not over
        self.pl = []  # player list
        self.rl = []  # rank list for players
        self.n_player_win_pos = 0  # current rank position 1,2,3,4  ( update after each player completes the game)

        for i in range(self.nplayers):   # initialize all player, by asking their name
            name = input(f"Enter the name for player {i+1}: ")
            self.pl.append(Player(name))

        self.start()  # begin the game
    def start(self):

        while(True and not(self.game_status)):

            for i in range(self.nplayers):
                self.play_turn(self.pl[i])
                if self.n_player_win_pos == ( self.nplayers - 1):  # game ends after n-1 players completed game

                    self.game_status = 1 # game is over

                    self.finish()
                    break
    def play_turn(self, player):
        if player.status != 1: # player not completed yet

            player.play()  # player rolls the dice and moves accordingly

            player.pos = self.board.dic.get(player.pos, player.pos)  # snake or ladder or nothing, move accordingly

            if player.pos >= 100: # if game completed by player
                player.pos = 100
                player.status = 1
                self.n_player_win_pos += 1  #  current rank in game
                player.rank = self.n_player_win_pos # assign player rank

            else:
                pass

    def finish(self):

        print("""  
                                        Game is OVER 
                                        Player postions are :
                                        """)
        print()
     
        for i in range(self.nplayers):

            if self.pl[i].status != 0:
                print(f"                      {self.pl[i].name}: {self.pl[i].rank}")
            else:
                print(f"                      {self.pl[i].name}: Lost the game")


        #        END

d = {4:25, 13:46, 42:63, 50:69, 62:81, 74:92,
     40:3, 22:5, 43:18, 54:31, 66:45, 89:53, 95:77, 99:41}
game_new = Game(4, d)
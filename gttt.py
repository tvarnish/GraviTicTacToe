# Gravity TicTacToe - GraviTicTacToe
# Thomas Varnish (C) 2015
import sys

class Game():
    board = [[0,0,0],
             [0,0,0],
             [0,0,0]] # 0 = EMPTY, 1 = O, 2 = X

    o, x = 1, 2
    o_name = ""
    o_score = 0
    
    x_name = ""
    x_score = 0

    playing = True

    def __init__(self):
        print "WELCOME TO...\n"
        print "\tGraviTicTacToe"
        print "\nPlay like you would normal TicTacToe (get three of your counters in  a  row,"
        print "vertically, diagonally or horizontally before your opponent), except in this"
        print "game, you have to watch out as after each round (once each  player  has  had"
        print "their turn), the  board  will  rotate, and  the  counters  will  drop  under"
        print "gravity. To win, you have to have three of your counters in a row before the"
        print "other player after the board has been rotated! If neither player has done so"
        print "before the board is filled, or if both players manage to do so at  the  same"
        print "time, then its a draw! Good Luck!\n"

    def assignPlayers(self, o_name="", x_name=""):
        if o_name == "":
            o_name = raw_input("Who is Player 1 ? > ")
            if raw_input("Is <%s> correct? Y/n > ").lower() in ["y", "ye", "yes"]:
                self.o_name = o_name
            else:
                o_name = raw_input("Who is Player 1 ? > ")
        else:
            self.o_name = o_name

        print

        if x_name == "":
            x_name = raw_input("Who is Player 2 ? > ")
            if raw_input("Is <%s> correct? Y/n > ").lower() in ["y", "ye", "yes"]:
                self.x_name = x_name
            else:
                x_name = raw_input("Who is Player 2 ? > ")
        else:
            self.x_name = x_name

        print

    def resetBoard(self):
         self.board = [[0,0,0],
                  [0,0,0],
                  [0,0,0]]

    def resetScores(self):
        self.o_score = 0
        self.x_score = 0

    def setBoard(self, board):
        self.board = board
        
    def turnBoard(self):
        print "\nTHE BOARD HAS FLIPPED!\n"
        # Apply Gravity #
        for i in range(3):
            temp = str(self.board[i][0]) + str(self.board[i][1]) + str(self.board[i][2])
            if "0" in temp:
                while temp[-1] == "0":
                    if temp[0] != "0" or temp[1] != "0":
                        temp = temp[-1] + temp[:-1]
                    else:
                        break
            self.board[i] = [int(temp[0]), int(temp[1]), int(temp[2])]
        for i in range(3):
            temp = str(self.board[i][0]) + str(self.board[i][1]) + str(self.board[i][2])
            if "0" in temp:
                while temp[1] == "0":
                    if temp[0] != "0" or temp[1] != "0":
                        temp = temp[1] + temp[:1] + temp[2]
                    else:
                        break
            self.board[i] = [int(temp[0]), int(temp[1]), int(temp[2])]
            
        # Rotate Board #
        new_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        
        for column in range(3):
            for row in range(3):
                new_board[column][row] = self.board[2 - row][column]
        self.board = new_board

    def displayBoard(self):
        for x in range(0,3):
            for y in range(0,3):
                if self.board[x][y] == 0:
                    print " - ",
                elif self.board[x][y] == 1:
                    print " O ",
                elif self.board[x][y] == 2:
                    print " X ",
            print
        print

    def getMove(self, player):
        if player == self.o_name:
            counter = self.o
        else:
            counter = self.x
        print "\n" + player + "'s Move... 0-2 Row, then 0-2 Column, no space e.g. 02"
        move = raw_input("  > ")

        retry = True
        while retry:
            try:
                while len(move) != 2 or move[0] not in ["0", "1", "2"] or move[0] not in ["0", "1", "2"]:
                    print "\nError - enter a valid move!"
                    move = raw_input("  > ")
                retry = False
            except:
                print "\nError - enter a valid move!"
                move = raw_input("  > ")

        retry = True
        while retry:
            try:
                while self.board[int(move[0])][int(move[1])] != 0:
                    print "\nError - that space is occupied!"
                    move = raw_input("  > ")
                retry = False
            except:
                print "\nError - enter a valid move!"
                move = raw_input("  > ")
        
        print
        self.board[int(move[0])][int(move[1])] = counter

    def checkDraw_filled(self):
        space_count = 0
        for i in range(3):
            if 0 in self.board[i]:
                space_count += 1
        if space_count == 0:
            print "\nIt's a DRAW! The board has been filled.\n"
            raw_input("Press Enter To Quit...")
            sys.exit()

    def checkWin(self):
        for i in range(3):
            # Horizontal
            if self.board[i][0] == self.board[i][1] and self.board[i][0] == self.board[i][2]:
                if self.board[i][0] == self.x:
                    print "\nCongratulations! %s WINS!\n" % self.x_name.upper()
                    raw_input("\nPress Enter to Quit...")
                    sys.exit()
                elif self.board[i][0] == self.o:
                    print "\nCongratulations! %s WINS!\n" % self.o_name.upper()
                    raw_input("\nPress Enter to Quit...")
                    sys.exit()

            # Vertical
            if self.board[0][i] == self.board[1][i] and self.board[0][i] == self.board[2][i]:
                if self.board[0][i] == self.x:
                    print "\nCongratulations! %s WINS!\n" % self.x_name.upper()
                    raw_input("\nPress Enter to Quit...")
                    sys.exit()
                elif self.board[0][i] == self.o:
                    print "\nCongratulations! %s WINS!\n" % self.o_name.upper()
                    raw_input("\nPress Enter to Quit...")
                    sys.exit()

        # Diagonal
        if self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2]:
            if self.board[0][0] == self.x:
                print "\nCongratulations! %s WINS!\n" % self.x_name.upper()
                raw_input("\nPress Enter to Quit...")
                sys.exit()
            elif self.board[0][0] == self.o:
                print "\nCongratulations! %s WINS!\n" % self.o_name.upper()
                raw_input("\nPress Enter to Quit...")
                sys.exit()

        if self.board[0][2] == self.board[1][1] and self.board[0][2] == self.board[2][0]:
            if self.board[0][2] == self.x:
                print "\nCongratulations! %s WINS!\n" % self.x_name.upper()
                raw_input("\nPress Enter to Quit...")
                sys.exit()
            elif self.board[0][2] == self.o:
                print "\nCongratulations! %s WINS!\n" % self.o_name.upper()
                raw_input("\nPress Enter to Quit...")
                sys.exit()

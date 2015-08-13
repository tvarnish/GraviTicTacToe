# Gravity TicTacToe - GraviTicTacToe
# Thomas Varnish (C) 2015
import time, gttt

g = gttt.Game()
g.assignPlayers()

while g.playing:
    g.displayBoard()
    g.checkWin()
    g.checkDraw_filled()
    g.getMove(g.o_name)
    g.displayBoard()
    time.sleep(0.5)
    g.checkDraw_filled()
    g.getMove(g.x_name)
    g.displayBoard()
    time.sleep(0.25)
    g.turnBoard()
    time.sleep(0.25)

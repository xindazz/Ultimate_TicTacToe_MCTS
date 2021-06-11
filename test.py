import numpy as np

from uttt import UltimateTicTacToe

# Basic test of UltimateTIcTacToe
o = 1
x = -1
size = 3
game = UltimateTicTacToe(size, o)

game.move((1, 1, 1, 1))

while not game.gameEnded():
    actions = game.validActions()
    action = np.random.randint(len(actions))
    game.move(actions[action])

print("Board: \n", game.board)
print("Score: \n", game.score)
print("Victor: ", game.victor)


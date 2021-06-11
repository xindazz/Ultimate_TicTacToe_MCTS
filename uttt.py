import numpy as np


class UltimateTicTacToe():
    o = 1
    x = -1
    
    # Action/Move format: (bigrow, bigcol, row, col)
    def __init__(self, size, next_to_move):
        self.size = size
        self.board = np.zeros((self.size, self.size, self.size, self.size)) # board of size x size x size x size
        self.next_to_move = next_to_move
        self.prev_move = None 
        self.score = np.zeros((self.size, self.size))
        self.victor = None

    def validActions(self):
        res = []
        if self.prev_move == None: # start of the game, any position is valid
            for idx, value in np.ndenumerate(self.board):
                res.append(idx)
        else:
            next_row, next_col = self.prev_move[2], self.prev_move[3] # row and col of next square
            for i in range(self.size):
                for j in range(self.size):
                    if self.board[next_row][next_col][i][j] == 0:
                        res.append((next_row, next_col, i, j))

            # if no valid move in target square, or if target square ended, any empty cell is valid
            if len(res) == 0 or self.score[next_row][next_col] != 0:
                for idx, value in np.ndenumerate(self.board):
                    if value == 0:
                        res.append(idx) 
        return res
            
    def move(self, action):
        # make the move
        bigrow, bigcol, row, col = action
        player = self.next_to_move
        self.board[bigrow][bigcol][row][col] = player
        self.next_to_move = -player
        self.prev_move = action

        # check if the move made ended the square
        row_win = np.sum(self.board[bigrow][bigcol][row, :]) == self.size * player
        col_win = np.sum(self.board[bigrow][bigcol][:, col]) == self.size * player
        diagl_win = (row == col) and (self.board[bigrow][bigcol].trace() == self.size * player)
        diagr_win = (row + col + 1 == self.size) and (self.board[bigrow][bigcol][::-1].trace() == self.size * player)

        # update score
        if row_win or col_win or diagl_win or diagr_win:
            self.score[bigrow][bigcol] = -self.next_to_move

    def gameEnded(self):
        rowsum = np.sum(self.score, 0)
        colsum = np.sum(self.score, 1)
        diag_sum_tl = self.score.trace()
        diag_sum_tr = self.score[::-1].trace()

        o_wins = any(rowsum == self.size)
        o_wins += any(colsum == self.size)
        o_wins += (diag_sum_tl == self.size)
        o_wins += (diag_sum_tr == self.size)

        # O wins
        if o_wins:
            self.victor = self.o
            return True

        x_wins = any(rowsum == -self.size)
        x_wins += any(colsum == -self.size)
        x_wins += (diag_sum_tl == -self.size)
        x_wins += (diag_sum_tr == -self.size)

        # X wins
        if x_wins:
            self.victor = self.x
            return True

        # Draw
        if len(self.validActions()) == 0:
            self.victor = 0
            return True

        # Game not finished
        return False

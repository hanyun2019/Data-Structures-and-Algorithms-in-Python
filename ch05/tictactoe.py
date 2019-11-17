# Haowen Huang refreshed on Nov 17, 2019
# Chapter 5: Array-Based Sequences: Multidimensional Data Sets
# /Users/Algorithms/python/dsa/ch05

# To properly initialize a two-dimensional list, 
# we must ensure that each cell of the primary list refers to an independent instance of a secondary list. 
# This can be accomplished through the use of Python’s list comprehension syntax.
# data=[[0]*c for j in range(r)]
# This command produces a valid configuration, similar to the one shown in Fig- ure 5.24. By using list comprehension, 
# the expression [0]*c is reevaluated for each pass of the embedded for loop. 
# Therefore, we get r distinct secondary lists, as desired. (We note that the variable j in that command is irrelevant; 
# we simply need a for loop that iterates r times.)


# data = [[0] * 3 for _ in range(5)]
# print("\n[[0]*3 for j in range(5)]: \n", data)

# Two-Dimensional Arrays and Positional Games
# Tic-Tac-Toe

class TicTacToe():
    """Management of a Tic-Tac-Toe game (does not do strategy)."""

    def __init__(self):
        """Start a new game."""
        self._board = [[' '] * 3 for j in range(3)]
        self._player = 'X'

    def mark(self, i, j):
        """Put an X or O mark at position(i,j) for next player's turn."""
        if not(0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError('Invalid board position')
        if self._board[i][j] != ' ':
            raise ValueError('Board position occupied')
        if self.winner() is not None:
            raise ValueError('Game is already complete')
        self._board[i][j] = self._player
        if self._player == 'X':
            self._player = 'O'
        else:
            self._player = 'X'

    def _is_win(self, mark):
        """Check whether the board configuration is a win for the given player."""
        board = self._board         # local variable for shorthand
        return (mark == board[0][0] == board[0][1] == board[0][2] or        # row 0
                mark == board[1][0] == board[1][1] == board[1][2] or        # row 1
                mark == board[2][0] == board[2][1] == board[2][2] or        # row 2
                mark == board[0][0] == board[1][0] == board[2][0] or        # column 0
                mark == board[0][1] == board[1][1] == board[2][1] or        # column 1
                mark == board[0][2] == board[1][2] == board[2][2] or        # column 2
                mark == board[0][0] == board[1][1] == board[2][2] or        # diagonal
                mark == board[0][2] == board[1][1] == board[2][0])          # rev diag
    
    def winner(self):
        """Return mark of winning player, or None to indicate a tie."""
        for mark in 'XO':
            if self._is_win(mark):
                return mark
        return None 

    def __str__(self):
        """Return string representation of current game board."""
        rows = ['|'.join(self._board[r]) for r in range(3)]
        return '\n-----\n'.join(rows)



if __name__ == "__main__":
    game = TicTacToe()
    # X moves:              # O moves:
    game.mark(1, 1);        game.mark(0, 2)
    game.mark(2, 2);        game.mark(0, 0)
    game.mark(0, 1);        game.mark(2, 1)
    game.mark(1, 2);        game.mark(1, 0)
    game.mark(2, 0)

    print(game)
    winner = game.winner()
    if winner is None:
        print('Tie')
    else:
        print(winner, 'wins')


    

    
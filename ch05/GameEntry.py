# Haowen Huang refreshed on Oct 17, 2019
# Chapter 5: Array-Based Sequences: Using Array-Based Sequences
# 基于数组的序列
# /Users/Algorithms/python/dsa/ch05

## 5.5 Using Array-Based Sequences
## 5.5.1 Storing High Scores for a Game

class GameEntry:
    """Represents one entry of a list of high scores."""
    
    def __init__(self, name, score):
        self._name = name
        self._score = score
    
    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def get_score(self):
        return self._score
    
    def __str__(self):
        return "({0}, {1})".format(self._name, self._score)       # e.g., '(Bob, 98)'



class Scoreboard:
    """Fixed-length sequence of high scores in nondecreasing oreder."""""
    
    def __init__(self, capacity=10):
        """ Initialize scoreboard with given maximum capacity.
        All entries are initially None."""    
        self._board = [None] * capacity             # reserve space for future scores
        self._n = 0                                 # number of actual entries
    
    def __getitem__(self, k):
        """Return entry at index k."""
        return self._board[k]

    def __str__(self):
        """Return string representation of the high score list."""
        return '\n'.join(str(self._board[j]) for j in range(self._n))
    
    def add(self, entry):
        """Consider adding entry to high scores."""
        score = entry.get_score()

        # Does new entry qualify as a high score?
        # answer is yes if board not full or score is higher than last entry
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):          # no score drops from list
                self._n += 1                        # so overall number increases

            # shift lower scores rightward to make room for new entry
            j = self._n - 1
            while j>0 and self._board[j-1].get_score() < score:
                self._board[j] = self._board[j-1]   # shift entry from j-1 to j
                j -= 1                              # and decrement j
            self._board[j] = entry                  # when done, add new entry    



if __name__ == "__main__":
    gameEntry1 = GameEntry("John", 100)
    print("\ngameEntry1: \n", gameEntry1)
    
    gameEntry2 = GameEntry("Mike", 1105)
    print("\ngameEntry2: \n", gameEntry2)

    gameEntry3 = GameEntry("Rose", 590)
    print("\ngameEntry3: \n", gameEntry3)

    gameEntry4 = GameEntry("Rob", 750)
    print("\ngameEntry4: \n", gameEntry4)

    gameEntry5 = GameEntry("Anna", 660)
    print("\ngameEntry5: \n", gameEntry5)

    gameEntry6 = GameEntry("Jack", 510)
    print("\ngameEntry6: \n", gameEntry6)

    
    scorelist = Scoreboard()
    scorelist.add(gameEntry1)
    scorelist.add(gameEntry2)
    scorelist.add(gameEntry3)
    scorelist.add(gameEntry4)
    scorelist.add(gameEntry5)
    scorelist.add(gameEntry6)
    print("\nscorelist: \n", scorelist)
    
    
    

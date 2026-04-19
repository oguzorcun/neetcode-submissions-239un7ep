
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def buildWord(w: str, i: int, j:int) -> bool:            
            if w == word:
                return True
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False
            if w + board[i][j] != word[:len(w) + 1]:
                return False

            w += board[i][j]
            board[i][j] = '/'
    
            found = (buildWord(w, i + 1, j)
                or buildWord(w, i - 1, j) 
                or buildWord(w, i, j + 1)
                or buildWord(w, i, j - 1))
            
            board[i][j] = w[-1]
            # w = w[:-1]

            return found

        for i in range(rows):
            for j in range(cols):
                if buildWord("", i, j):
                    return True

        return False

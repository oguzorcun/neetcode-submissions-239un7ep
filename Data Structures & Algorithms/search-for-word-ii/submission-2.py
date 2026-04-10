class Trie:
    def __init__(self):
        self.children = {}
        self.end = False
        self.word = ""
        
    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.end = True    
        cur.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie()
        for w in words:
            t.insert(w)

        rows, cols, res = len(board), len(board[0]), []

        def find(i: int, j: int, t: Trie):
            nonlocal res
            if t.end:
                res.append(t.word)
                t.end = False
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            c = board[i][j]
            if c not in t.children:
                return

            board[i][j] = '/'

            find(i + 1, j, t.children[c])
            find(i - 1, j, t.children[c])
            find(i, j + 1, t.children[c])
            find(i, j - 1, t.children[c])

            board[i][j] = c

        for row in range(rows):
            for col in range(cols):
                find(row, col, t)
        return res













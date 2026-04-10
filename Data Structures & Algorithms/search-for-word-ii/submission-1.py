class Trie:
    def __init__(self):
        self.children = {}
        self.end = False
        
    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.end = True    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie()
        for w in words:
            t.insert(w)

        rows, cols, res = len(board), len(board[0]), []

        def find(i: int, j: int, w: str, t: Trie):
            nonlocal res
            if t.end:
                res.append(w)
                t.end = False
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            c = board[i][j]
            if c not in t.children:
                return

            w += c
            board[i][j] = '/'

            find(i + 1, j, w, t.children[c])
            find(i - 1, j, w, t.children[c])
            find(i, j + 1, w, t.children[c])
            find(i, j - 1, w, t.children[c])

            # backtrackkk
            board[i][j] = w[-1]
            w = w[:-1]

        for row in range(rows):
            for col in range(cols):
                find(row, col, "", t)
        return res













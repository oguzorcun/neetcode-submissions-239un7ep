class WordDictionary:
    def __init__(self):
        self.childs = {}
        self.end = False

    def addWord(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.childs:
                cur.childs[c] = WordDictionary()
            cur = cur.childs[c]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            if c not in cur.childs:
                return False
            cur = cur.childs[c]
        return cur.end

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = WordDictionary()
        for w in wordDict: d.addWord(w)

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and d.search(s[j:i]): 
                    dp[i] = True

        print(dp)
        return dp[-1]
























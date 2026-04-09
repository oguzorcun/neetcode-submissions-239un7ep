class PrefixTree:

    def __init__(self):
        self.children = {}
        self.end = False
        
    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = PrefixTree()
            cur = cur.children[c]
        cur.end = True    

    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return True
        
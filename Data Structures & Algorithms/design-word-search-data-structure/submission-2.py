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
        for i, c in enumerate(word):
            if c != '.' and c not in cur.childs:
                return False
            if c == '.':
                for child in cur.childs.values():
                    if child.search(word[i+1:]):
                        return True
                return False
            cur = cur.childs[c]
        return cur.end

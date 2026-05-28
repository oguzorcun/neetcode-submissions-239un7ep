class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        chars = defaultdict(deque)
        for i, c in enumerate(t):
            chars[c].append(i)

        cur = 0
        for c in s:
            if c not in chars or not chars[c]: return False
            i = chars[c].popleft()
            while i < cur and chars[c]:
                i = chars[c].popleft()
            if i < cur: return False
            cur = i

        return True
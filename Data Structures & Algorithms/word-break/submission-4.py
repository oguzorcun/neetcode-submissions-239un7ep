class Solution:
    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s) + 1):
            for w in wordDict:
                if dp[i] and s[i : i + len(w)] == w:
                    dp[i + len(w)] = True

        return dp[-1]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in d: 
                    dp[i] = True
                    break

        return dp[-1]
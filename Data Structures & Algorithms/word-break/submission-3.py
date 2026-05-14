class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s) + 1):
            for w in wordDict:
                if dp[i] and s[i : i + len(w)] == w:
                    dp[i + len(w)] = True

        return dp[-1]


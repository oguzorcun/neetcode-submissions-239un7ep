class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        s = []
        ans = [0] * len(temperatures) 

        for i, t in enumerate(temperatures):
            while s and temperatures[s[-1]] < t:
                colder_day = s.pop()
                ans[colder_day] = i - colder_day
            s.append(i)

        return ans
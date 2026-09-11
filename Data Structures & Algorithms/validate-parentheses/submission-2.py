class Solution:
    def isValid(self, s: str) -> bool:
        matching = {'(':')', '[':']', '{':'}'}
        stack = []

        for c in s:
            if c in matching:
                stack.append(c)
            elif not stack or c != matching[stack.pop()]: 
                return False
        
        return not stack
        
class Solution:
    def isValid(self, s: str) -> bool:
        matching = {'(':')', '[':']', '{':'}'}
       

        stack = []

        for c in s:
            if c in matching:
                stack.append(c)
                continue
            if not stack: return False
            popped = stack.pop()
            if c != matching[popped]: return False
        
        return True if not stack else False
            

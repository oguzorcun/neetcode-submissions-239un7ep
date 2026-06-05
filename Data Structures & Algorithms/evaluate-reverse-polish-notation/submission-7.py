class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        ops = ['+', '-', '*', '/']

        for t in tokens:
            print(t,s)
            if t not in ops: s.append(int(t))
            elif t == '+':
                s.append(s.pop() + s.pop())
            elif t == '-':
                s.append(-s.pop() + s.pop())
            elif t == '*':
                s.append(s.pop() * s.pop())
            elif t == '/':
                divisor, dividend = s.pop(), s.pop()
                s.append(int(dividend / divisor))
        
        return s[0]
                

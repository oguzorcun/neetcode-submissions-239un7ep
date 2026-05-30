class MinStack:

    def __init__(self):
        self.s = []
        self.p = []

    def push(self, val: int) -> None:
        self.s.append(val)
        self.p.append(min(self.p[-1], val) if self.p else val) 

    def pop(self) -> None:
        self.s.pop()
        self.p.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.p[-1]





class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len([0 for p in details if int(p[11:13]) > 60])
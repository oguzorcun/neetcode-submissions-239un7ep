class Solution:

    def lenTriDigits(self, s: str) -> str:
        l = len(s)

        if l < 10:
            return f"00{l}"
        elif l < 100:
            return f"0{l}"
        else:
            return str(l)

    def encode(self, strs: List[str]) -> str:
        encoded = str()
        for s in strs:
            encoded = ''.join([encoded, self.lenTriDigits(s), s])
        return encoded


    def decode(self, s: str) -> List[str]:

        i = 0
        strs = []

        while i < len(s):
            l = int(s[i:i+3])
            strs.append(s[i+3:i+3+l])
            i += l + 3

        return strs
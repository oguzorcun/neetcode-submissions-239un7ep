class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        str_lengths = ""
        for s in strs:
            encoded += s
            str_lengths += "|" + str(len(s))
        return str(len(strs)) + str_lengths + "|" + encoded

    def decode(self, s: str) -> List[str]:
        count = int(s.split('|', 1)[0])
        count_lens_encoded = s.split('|', 1 + count)
        encoded = count_lens_encoded[-1]
        lens = count_lens_encoded[1:-1]

        decoded_strs = []
        index = 0
        for l in lens:
            decoded = ""
            for i in range(index, index + int(l)):
                decoded += encoded[i]
            index += int(l)
            decoded_strs.append(decoded)

        return decoded_strs
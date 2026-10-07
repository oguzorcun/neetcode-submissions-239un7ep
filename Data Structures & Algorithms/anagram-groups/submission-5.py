class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            encode = [0] * 26
            for c in s: encode[ord(c) - ord('a')] += 1
            d[tuple(encode)].append(s)

        return list(d.values())
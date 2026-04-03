class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1

        frequency_bucket = [[] for _ in range(len(nums)+1)]

        for n, c in count.items():
            frequency_bucket[c].append(n)

        res = []

        for i in range(len(frequency_bucket) - 1, 0, -1):
            for n in frequency_bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res

        return res

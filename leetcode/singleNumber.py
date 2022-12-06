from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        L, d = len(nums), {}
        for n in nums:
            if n in d:
                del d[n]
            else:
                d[n] = 1
        return list(d)[0]

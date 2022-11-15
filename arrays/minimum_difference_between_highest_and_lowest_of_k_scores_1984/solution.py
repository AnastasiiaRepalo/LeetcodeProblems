from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_dif = float('inf')
        for i in range(len(nums)-k+1):
            min_dif = min(min_dif, nums[i+k-1]-nums[i])
        return min_dif


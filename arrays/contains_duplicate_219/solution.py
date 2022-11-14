from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = dict()
        for i, el in enumerate(nums):
            if el in hashmap and abs(hashmap[el] - i) <= k:
                return True
            hashmap[el] = i
        return False
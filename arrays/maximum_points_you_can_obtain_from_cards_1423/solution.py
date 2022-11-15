from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        max_sum = cur_sum = sum(cardPoints[:k])
        for i in range(k - 1, -1, -1):
            cur_sum -= cardPoints[i]
            cur_sum += cardPoints[i - k]
            max_sum = max(max_sum, cur_sum)
        return max_sum

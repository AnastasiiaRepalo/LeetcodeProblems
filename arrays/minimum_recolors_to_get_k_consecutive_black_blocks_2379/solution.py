class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_count = count = blocks[:k].count('W')
        for i in range(len(blocks) - k):
            count -= (blocks[i] == 'W')
            count += (blocks[i+k] == 'W')
            min_count = min(min_count, count)
        return min_count
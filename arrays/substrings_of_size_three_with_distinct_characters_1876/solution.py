class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        counter = 0
        for i in range(len(s)-3):
            string = s[i:i+4]
            if len(set(string)) == 3:
                counter += 1

        return counter




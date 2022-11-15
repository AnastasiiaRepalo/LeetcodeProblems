class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ''
        hashset = set(s)
        for i, el in enumerate(s):
            if not (el.lower() in hashset and el.upper() in hashset):
                left_str = self.longestNiceSubstring(s[:i])
                right_str = self.longestNiceSubstring(s[i+1:])
                if len(left_str) > len(right_str):
                    return left_str
                else:
                    return right_str
        return s




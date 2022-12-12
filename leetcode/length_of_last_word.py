class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_str = s.split()
        return len(new_str[-1])

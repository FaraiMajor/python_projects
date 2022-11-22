class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return False if x < 0 else x == int(str(x)[::-1])
        return str(x)[::-1] == str(x)

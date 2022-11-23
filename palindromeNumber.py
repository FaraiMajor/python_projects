class Solution:

    def __init__(self, num) -> None:
        self.num = num
    # def isPalindrome(self, x: int) -> bool:
    #     # return False if x < 0 else x == int(str(x)[::-1])
    #     return str(x)[::-1] == str(x)

    def isPalindrome(self) -> bool:
        x = self.num
        reverse_x = ""
        for i in str(x):
            reverse_x = i + reverse_x
        if reverse_x == str(x):
            return True
        else:
            return False


palindrome = Solution(121)
print(palindrome.isPalindrome())

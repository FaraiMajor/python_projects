'''
Given a string s, return the longest palindromic substring in s.
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Palindrome
        # s == s[::-1]
        # "cbbd"
        #   make a driver fucntion to get palindrome

        p = ''
        for i in range(len(s)):
            p1 = self.get_palindrome(s, i, i+1)
            p2 = self.get_palindrome(s, i, i)
            p = max([p, p1, p2], key=len)

        return p

    def get_palindrome(self, str, left, right):
        while left >= 0 and right < len(str) and str[left] == str[right]:
            left -= 1
            right += 1

        return str[left+1:right]


# 2 same thing but longer
def longest_palindromic_substring(s):
    longest_palindrome = ""
    for i in range(len(s)):
        # Check for odd-length palindromes
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        current_palindrome = s[left+1:right]
        if len(current_palindrome) > len(longest_palindrome):
            longest_palindrome = current_palindrome
        # Check for even-length palindromes
        left, right = i, i+1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        current_palindrome = s[left+1:right]
        if len(current_palindrome) > len(longest_palindrome):
            longest_palindrome = current_palindrome
    return longest_palindrome


'''
Here's one way to solve the problem:

Initialize a variable to keep track of the longest palindromic substring found so far. 
Initially, it can be an empty string.
Loop through the string s and, for each character, expand around it to find the longest 
palindromic substring centered at that character. This can be done by checking if the 
characters to the left and right of the current character match, and continuing to expand 
until they don't.
Compare the length of the current palindromic substring found to the length of the longest 
one found so far. If it's longer, update the longest palindromic substring found so far.
After looping through the whole string, return the longest palindromic substring found.
Here's the code to implement this approach in Python:
'''

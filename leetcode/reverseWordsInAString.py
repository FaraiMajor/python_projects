class Solution:
    def reverseWords(self, s: str) -> str:
        return (" ".join(s.split()[::-1]))


'''
split string into an array of words
reverse the array
use join to return back a string
'''

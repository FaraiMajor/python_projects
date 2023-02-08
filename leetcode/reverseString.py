from typing import List


def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """

    l = 0
    r = len(s)-1
    while (l < r):
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return s


s = ['f', 'a', 'r', 'a', 'i']

print(reverseString(s))

print(s[::-1])

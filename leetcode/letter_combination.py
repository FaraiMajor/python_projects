
def letterCombinations(digits):
    if len(digits) == 0:
        return []
    letters = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
    res = []

    def backtrack(k, curr):
        if len(curr) == len(digits):
            res.append(curr)
            return
        for ch in letters[digits[k]]:
            backtrack(k+1, curr+ch)
    backtrack(0, '')
    return res


digits = "23"
print(letterCombinations(digits))

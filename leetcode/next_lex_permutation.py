'''
given a word, return the next alphabetically greater string in all 
permutations of that word. if there is no greater permutation, return the string 
'no answer' instead.
'''


def rearrangeWord(word):
    word_list = list(word)
    # Find non-increasing suffix
    i = len(word_list)-1
    while i > 0 and word_list[i-1] >= word_list[i]:
        i -= 1
    if i <= 0:
        return 'no answer'
    # Find the rightmost successor to pivot in the suffix
    j = len(word_list) - 1
    while word_list[j] <= word_list[i - 1]:
        j -= 1
    # Swap the pivot with the rightmost character
    word_list[i-1], word_list[j] = word_list[j], word_list[i-1]
    # Reverse the sufix
    # word_list[i:] = word_list[len(word_list)-1:i-1:-1]
    word_list[i:] = reversed(word_list[i:])
    return ''.join(word_list)


if __name__ == '__main__':
    word = input("Enter String Value: ")
    result = rearrangeWord(word)
    print(result)

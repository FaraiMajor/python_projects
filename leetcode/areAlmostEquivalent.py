def areAlmostEquivalent(s, t):
    n = len(s)
    result = []
    for i in range(n):
        string1 = s[i]
        string2 = t[i]
        if len(string1) != len(string2):
            result.append("NO")
            continue
        flag = True
        for j in 'abcdefghijklmnopqrstuvwxyz':
            if abs(string1.count(j) - string2.count(j)) > 3:
                flag = False
                break
        if flag:
            result.append("YES")
        else:
            result.append("NO")
    print(string1)
    return result


s = ['aabaab', 'aaaaabb']
t = ['bbabbc', 'abb']

print(areAlmostEquivalent(s, t))

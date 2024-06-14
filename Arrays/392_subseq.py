def isSubsequence(s, t):
    index_array = []
    for l in s:
        if l in t:
            index_array.append(t.index(l))
            t = t.replace(l, '', 1)
        else:
            return False

    first = index_array
    index_array.sort()
    print(first)
    print('Hi')
    return first ==  index_array

ans = isSubsequence('abc', 'aghbtyc')
print(ans)
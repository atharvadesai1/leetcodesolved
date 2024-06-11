def repeatedSubstringPattern(s):
        if len(s) == 0 or len(s) == 1:
            return False

        doubled_s = (s + s)[1:-1]
        return s in doubled_s

ans = repeatedSubstringPattern('abcdaabcda')
print(ans)
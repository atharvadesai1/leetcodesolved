array_substring = []
def subsequence(s,tempstring,i):
    if i == len(s):
        array_substring.append(tempstring)
        return 

    # take
    subsequence(s, str(tempstring+s[i]) , i+1)
    # not take
    subsequence(s, tempstring, i+1)
    return 
t = 'abc'
s = 'abcdbncpqa'
subsequence(s,'',0)

print(array_substring)
print(f'Total Count of subsequence {t} is {array_substring.count(t)}')
def titleToNumber(columnTitle):
    dict = {}
    asci = 65
    k=0
    ans = 0
    for i in range(1,27):
        dict[chr(asci)] = i
        asci+=1

    for i in range(len(columnTitle)-1,-1,-1):
        value = dict[columnTitle[i]]
        ans += (26**k)*value
        k+=1
    return ans

ans = titleToNumber(input('Enter the Title Number: '))
print(f'Answer: {ans}')
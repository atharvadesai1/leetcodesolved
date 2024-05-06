def largeGroupPositions(s):
    if len(s) < 3:
        return []

    master = []
    count = 1
    i=1
    flag = True
    while i < len(s):
        while i < len(s) and s[i] == s[i-1]:
                if flag:
                    start = i-1
                count += 1
                i += 1
                flag = False
        
        if count > 2:
            end = i-1
            master.append([start,end])
        
        count = 1
        flag = True
        i+=1
    return master
            

s = 'aabbbbcccdddeejfgtttssp'
ans = largeGroupPositions(s)
print(f'Ans: {ans}')

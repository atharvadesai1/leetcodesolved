main = 'atharvadesai'
sub = 'ads'
solution = []
max_len = [-1]
def maxlen(index, main, sub, st):
    if index == len(main):
        # print("ST "+ st)
        # print("SUB "+ sub)
        if len(sub) <= len(st):
            if sub in st:
                if len(st) >= max_len[0]:
                    max_len[0] = len(st)
                    solution.append(st)
                return
            else:
                return
        else:
            return 
    
    maxlen(index+1, main, sub, st + main[index])
    maxlen(index+1, main, sub, st)
    return max_len[0]

ans = maxlen(0, main, sub, '')
print(ans)
print(solution)



    

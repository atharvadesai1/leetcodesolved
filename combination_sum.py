solution = []
array = [8,7,4,3]
array.sort()
target = 11

def combination(t, i, stack):
    if i == len(array):
        return
    
    if t == 0:
        solution.append(stack)
        return 
    
    if t < array[i]:
        return
    # take
    combination(t-array[i], i, stack + [array[i]])
    # not take
    combination(t, i+1, stack)

    return solution
ans  = combination(target, 0, [])
print(ans)
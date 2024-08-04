solution = []
arr= [5, 2, 1]
def subset(i, total):
    if i == len(arr):
        solution.append(total)
        return 
    #  take
    # solution.append(total)
    subset(i+1, total+arr[i])
    subset(i+1, total)

    return solution
ans = subset(0, 0)
ans.sort()
print(ans)
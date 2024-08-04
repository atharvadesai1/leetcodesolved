A = [5,7,8,9,12,13]
P = [[1,3], [2,3], [3,4]]
def rangesum(A, P):
    sum_val = 0
    while P:
        current = P.pop(0)
        i = current[0]-1 
        j = current[1]
        new_array = A[:i] + A[j:]
        print(new_array)
        sum_val += len(new_array)

    return sum_val

ans = rangesum(A,P)
print(ans)


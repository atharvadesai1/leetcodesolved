
def majorityElement(nums):
    hash = {}
    visited = []
    for e in nums:
        if e not in visited:
            visited.append(e)
            hash[e] = 1
        else:
            hash[e] += 1
    
    max_val = -1 
    max_num = -1
    for e in hash:
        if hash[e] > max_val:
            max_val = hash[e]
            max_num = e
    
    return max_num

array = [2,2,1,1,1,2,2]
ans = majorityElement(array)
print(ans)

print("Done!!")
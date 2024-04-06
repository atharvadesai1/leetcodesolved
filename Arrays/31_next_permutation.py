nums = [1,5,1]
for i in range(len(nums)-2, -1 ,-1):
    if nums[i] >= nums[i+1]:
        i -= 1
    else:
        break

ind = i
print(ind)
if i!=-1:
    jin = -1
    maxi = 9999

    for j in range(i+1, len(nums)):
        if nums[j] <= maxi and nums[j] > nums[ind]:
            maxi = nums[j]
            jin = j

    if maxi!= 9999 or jin!=-1:
        nums[ind], nums[jin] = nums[jin], nums[ind]

print(jin)
start = ind+1 
end = len(nums)-1

while start < end:
    nums[start], nums[end] = nums[end], nums[start]
    start +=1
    end -= 1

print(nums)
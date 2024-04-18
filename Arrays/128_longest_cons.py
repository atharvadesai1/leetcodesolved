def longestConsecutive(nums):
    if not nums:
        return 0

    nums.sort()
    max_size = 1
    count = 0
    for i in range(len(nums)-1):
        if nums[i+1] == nums[i] + 1:
            count += 1
        elif nums[i+1] == nums[i]:
            continue
        else:
            count += 1
            if count > max_size:
                max_size = count
            count = 0
        
    if count >= max_size:
        count += 1
        max_size = count

    return max_size

nums = [7,8,2,1,5,3,4,51,52,19,20,21]
ans = longestConsecutive(nums)
print(f'Size of Longest Consecutive Array: {ans}')
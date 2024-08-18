def jump(nums):
    l = 0
    r = 0
    count = 0
    while r<len(nums)-1:
        if l == 0 and r == 0:
            l += 1
            r += nums[r]
            count += 1
            print(str(l) + " " + str(r))
            continue
        
        max_val = -1
        for i in range(l, r+1):
            if nums[i] + i > max_val:
                max_val = nums[i] + i

        if max_val > len(nums):
            max_val = len(nums)-1
        
        l = r + 1
        r = max_val  
        count += 1
    
    return count


nums = [4,1,1,3,1,1,1]
ans = jump(nums)
print(ans)

        

        

            

    
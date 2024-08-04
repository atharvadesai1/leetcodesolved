supers_set = set()
supers_set.add('[]')
def possible_subset(nums, i):
    if len(nums) == 1 or i == len(nums):
        nums = [str(x) for x in nums]
        supers_set.add(str(nums))
        return
    else:
        nums = [str(x) for x in nums]
        supers_set.add(str(nums))

    # nums[i] is present
    possible_subset([x for x in nums if x!=nums[i]], i)
    possible_subset(nums, i+1)

    return supers_set

i = 0
nums = [17,2,3,4]
ans = possible_subset(nums, i)
# array = [[]]
# for num_str in ans:
#     subarray = [x for x in num_str]
#     array.append([int(x) for x in subarray])

print(ans)
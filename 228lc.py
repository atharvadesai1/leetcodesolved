print('Enter the array: ')
nums = list(map(int, input().split()))
nums.sort()
print(f'Sorted Array: {nums}')
subarray = ''
main = []
for i in range(1, len(nums)):
    if nums[i] == nums[i-1]+1:
        if len(subarray) == 0:
            subarray += str(nums[i-1]) + '->'
        else:
            continue
    else:
        subarray += str(nums[i-1])
        main.append(subarray)
        subarray = ''

subarray += str(nums[-1])
main.append(subarray)

print(f'Summary Ranges: {main}')
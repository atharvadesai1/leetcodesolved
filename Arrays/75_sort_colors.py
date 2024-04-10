nums = [2,0,2,1,1,0]
red = 0
white = 0 
blue = 0

new_array = []

for elements in nums:
    if elements == 0:
        red += 1
    elif elements == 1:
        white += 1
    elif elements == 2:
        blue += 1
    
k=0
len_red = red

while k < len_red:
    nums[k] = 0
    k +=1

len_white = white + k
while k < len_white:
    nums[k] = 1
    k+=1

len_blue = blue + k
while k < len_blue:
    nums[k] = 2
    k+=1



print(nums)

# nums = [9,43,21,54,7,65,32,111]
# for i in range(len(nums)-1):
#     min_element = nums[i]
#     for j in range(i, len(nums)):
#         if nums[j] < min_element:
#             min_element = nums[j]
#             min_index = j
        
#     if min_element != nums[i]:
#         nums[i], nums[min_index] = nums[min_index], nums[i]
# print(nums)
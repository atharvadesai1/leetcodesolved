matrix = [1,3,5,7,10,11,16,20,23,30,34,60]
target = 3
start = 0
end = len(matrix) - 1

while start <= end:
    mid = (start + end) // 2
    if matrix[mid] == target:
        print(f'{True} index:{mid}')
        break
    elif matrix[mid] > target:
        end = mid - 1
    elif matrix[mid] < target:
        start = mid + 1

print(f'{False} Element not present')
    

def searchMatrix(matrix, target):
    start = 0
    end = len(matrix) * len(matrix[0]) - 1

    while start <= end:
        mid_index = (start + end)//2
        i = mid_index // len(matrix[0])
        j = mid_index % len(matrix[0])
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            end = mid_index - 1
        elif matrix[i][j] < target:
            start = mid_index + 1
        
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
value = searchMatrix(matrix, target)
print(value)
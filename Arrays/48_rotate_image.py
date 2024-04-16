matrix = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(matrix[0])-1):
    for j in range(i+1, len(matrix[0])):
        matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]
    
for k in range(len(matrix[0])):
    start = 0 
    end = len(matrix[0])-1
    while start < end:
        matrix[k][start], matrix[k][end] = matrix[k][end], matrix[k][start]
        start += 1
        end -= 1
    
print(matrix)
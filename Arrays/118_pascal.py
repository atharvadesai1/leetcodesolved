def generate(numRows):
    if numRows == 0:
        return []

    array = [[] for _ in range(numRows)]
    if numRows == 1:
        array[0].append(1)
        return array
    array[0].append(1)
    for i in range(1,numRows):
        array[i].append(1)
        for j in range(len(array[i-1])-1):
            array[i].append(array[i-1][j] + array[i-1][j+1])
        array[i].append(1)
    
    return array


numRows = int(input('Enter number of rows: '))
ans = generate(numRows)
print(f"'Pascal's Triangle: {ans}")

def spiralOrder(matrix):
    ans = []
    top = 0
    bottom = len(matrix)-1
    left = 0
    right = len(matrix[0])-1
    while True:
        if len(ans) >= len(matrix)*len(matrix[0]):
            break
        if left > right:
            pass
        else:
            for i in range(left, right+1):
                ans.append(matrix[top][i])


        if len(ans) >= len(matrix)*len(matrix[0]):
            break
        if top >= bottom:
            pass
        else:
            for i in range(top+1, bottom+1):
                ans.append(matrix[i][right])


        if len(ans) >= len(matrix)*len(matrix[0]):
            break
        if left >= right:
            pass
        else:
            for i in range(right-1, left-1, -1):
                ans.append(matrix[bottom][i])
                print(matrix[bottom][i])


        if len(ans) >= len(matrix)*len(matrix[0]):
            break
        if top >= bottom-1:
            pass
        else:
            for i in range(bottom-1, top, -1):
                ans.append(matrix[i][left])
        
        top += 1
        right -= 1
        bottom -= 1
        left += 1
        print("iteration")
        print(str(top) + str(right) + str(bottom) + str(left))
        if len(ans) >= len(matrix)*len(matrix[0]):
            break

    return ans  

matrix = [[1,2,3],[4,5,6],[7,8,9]]
ans = spiralOrder(matrix)
print(ans)

    
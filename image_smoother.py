# 661. Image Smoother
# An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).

def imageSmoother(img):
    m = len(img)
    n = len(img[0])
    if m==1 and n==1:
        return img
        
    matrix = [[-1 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            center = img[i][j]
            if i != 0:
                north = img[i-1][j]
            else:
                north = 0
            
            if i != 0 and j != 0:
                north_west = img[i-1][j-1]
            else:
                north_west = 0
            
            if i != 0 and j != n-1:
                north_east = img[i-1][j+1]
            else:
                north_east = 0
            
            if i != m-1:
                south = img[i+1][j]
            else:
                south = 0
            
            if i != m-1 and j != 0:
                south_west = img[i+1][j-1]
            else:
                south_west = 0
            
            if i != m-1 and j != n-1:
                south_east = img[i+1][j+1]
            else:
                south_east = 0

            if j != 0:
                west = img[i][j-1]
            else:
                west = 0
            
            if j != n-1:
                east = img[i][j+1]
            else:
                east = 0

            

            if (m==1 or n==1) and (j==0 or j==n-1) and (i==0 or i==m-1):
                matrix[i][j] = (north + south + west + east + center)//2

            elif (m==1 or n==1) and ((j!=0 and j!=n-1) or (i!=0 and i!=m-1)):
                    matrix[i][j] = (north + south + west + east + center)//3

            elif (i == 0 and j == 0) or (i==0 and j==n-1) or (i == m-1 and j == 0) or (i==m-1 and j==n-1):
                matrix[i][j] = (north + north_west + north_east + south + south_west + south_east + west + east + center)//4
            
            elif (i==0 and j!=0 and j!=n-1) or (i==m-1 and j!=0 and j!=n-1) or (j==0 and i!=0 and i!=m-1) or (j==n-1 and i!=0 and i!=m-1):
                matrix[i][j] = (north + north_west + north_east + south + south_west + south_east + west + east + center)//6
            
            else:
                matrix[i][j] = (north + north_west + north_east + south + south_west + south_east + west + east + center)//9

    return matrix


img = [[100,200,100],[200,50,200],[100,200,100]]
ans  = imageSmoother(img)
print(ans)

    
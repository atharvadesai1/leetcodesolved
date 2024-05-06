def isRectangleOverlap(rec1, rec2):
    # Check if the x-ranges overlap
    x_overlap = not (rec1[2] <= rec2[0] or rec2[2] <= rec1[0])
    
    # Check if the y-ranges overlap
    y_overlap = not (rec1[3] <= rec2[1] or rec2[3] <= rec1[1])
    
    # Return true if both x and y ranges overlap
    return x_overlap and y_overlap

rec1 = [0,0,2,2]
rec2 = [1,1,3,3]
ans = isRectangleOverlap(rec1, rec2)

if ans:
    print('The Rectangle Overlap')
else:
    print('Rectangle does not Overlap')

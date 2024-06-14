def minMovesToSeat(seats, students):
    seats.sort()
    students.sort()
    
    # Calculate the total moves required
    total_moves = 0
    for i in range(len(seats)):
        total_moves += abs(seats[i] - students[i])
    
    return total_moves


ans = minMovesToSeat([4,1,5,9], [1,3,2,6])
print(ans)

#-1 6 -1
#
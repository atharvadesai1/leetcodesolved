def merge(intervals):
    if len(intervals) == 1 or len(intervals) == 0:
        return intervals

    sorted_intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
    #intially sorting the intervals based on 
    new_array = list()
    gate = False
    i = 0
    j = 1
    pseudo_array = sorted_intervals[i]
    while j < len(intervals):
        if pseudo_array[1] >= sorted_intervals[j][0]:
            pseudo_array = [sorted_intervals[i][0], max(sorted_intervals[j][1], pseudo_array[1])]
            j += 1
            gate = True
        else:
            new_array.append(pseudo_array)
            i = j 
            j = i + 1
            pseudo_array = sorted_intervals[i]
            gate = False

    if not new_array:
        new_array.append(pseudo_array)
    elif gate:
        new_array.append(pseudo_array)
    if pseudo_array  == sorted_intervals[-1] and i==len(intervals)-1 and j==len(intervals):
        new_array.append(pseudo_array)

    return new_array

sorted_intervals = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
new_interval = merge(sorted_intervals)
print(new_interval)


# Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n. If there are no two adjacent 1's, return 0.

# Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the absolute difference between their bit positions. For example, the two 1's in "1001" have a distance of 3.

 

# Example 1:

# Input: n = 22
# Output: 2
# Explanation: 22 in binary is "10110".
# The first adjacent pair of 1's is "10110" with a distance of 2.
# The second adjacent pair of 1's is "10110" with a distance of 1.
# The answer is the largest of these two distances, which is 2.
# Note that "10110" is not a valid pair since there is a 1 separating the two 1's underlined.
# Example 2:

# Input: n = 8
# Output: 0
# Explanation: 8 in binary is "1000".
# There are not any adjacent pairs of 1's in the binary representation of 8, so we return 0.
# Example 3:

# Input: n = 5
# Output: 2
# Explanation: 5 in binary is "101".
 

# Constraints:

# 1 <= n <= 109


def binaryGap(n):
    binary_list = []
    div = n

    while div != 0:
        binary_list.append(str(div%2))
        div = div // 2

    binary_list.reverse()
    binary_string = ''.join(binary_list)
    print(f'Binary of {n} is {binary_string}')

    max_dist = 0
    i = 0
    timer = 0
    initiated = True
    while i< len(binary_string):
        if binary_string[i] == '1':
            timer += 1

        if timer == 1 and initiated:
            start = i 
            initiated = False
        
        if timer == 2:
            end = i 
            if (end- start) > max_dist:
                max_dist = (end- start)
            start = i
            timer = 0
            initiated = True
            continue

        i += 1                           

    return max_dist   


n = 22
ans = binaryGap(n)
print(f'Max distance between 1 of binaries is {ans}')

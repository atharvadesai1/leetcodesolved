def longestsubstring(s):
    substring = []
    visited = []
    for i in range(len(s)-1):
        substring.append(s[i])
        visited.append(s[i])
        for j in range(i+1, len(s)):
            if s[j] not in visited:
                visited.append(s[j])
                sub_str = ''.join(visited)
                substring.append(sub_str)
            else:
                visited = []
                break
        if visited:
            break

    print(substring)
    max_count = 0
    for string in substring:
        if len(string) > max_count:
            max_count = len(string)
    
    return max_count

ans = longestsubstring('dvdf')
print(ans)

# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         char_index_map = {}
#         max_length = 0
#         start = 0

#         for end in range(len(s)):
#             if s[end] in char_index_map:
#                 # Move the start pointer to the right of the last occurrence of s[end]
#                 start = max(start, char_index_map[s[end]] + 1)
#             # Update the last occurrence of the character
#             char_index_map[s[end]] = end
#             # Calculate the length of the current substring
#             max_length = max(max_length, end - start + 1)

#         return max_length

def reverseVowels(s):
        vowels = 'aeiouAEIOU'
        s_array = [l for l in s]
        for i in range(len(s_array)-1):
            if s_array[i] in vowels:
                for j in range(i+1, len(s_array)):
                    if s_array[j] in vowels:
                        s_array[i] , s_array[j] = s_array[j] , s_array[i]
            else:
                continue

        return ''.join(s_array)


# def reverseVowels(s):
#         vowels = 'aeiouAEIOU'
#         s_array = list(s)
#         left, right = 0, len(s) - 1

#         while left < right:
#             while left < right and s_array[left] not in vowels:
#                 left += 1
#             while left < right and s_array[right] not in vowels:
#                 right -= 1
#             if left < right:
#                 s_array[left], s_array[right] = s_array[right], s_array[left]
#                 left += 1
#                 right -= 1

#         return ''.join(s_array)


ans = reverseVowels('hello')
print(ans)
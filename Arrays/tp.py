nums = [3,2,3,5,1,3,2,6,6,6,6]
dictionary = dict()
for number in nums:
    if number not in dictionary:
        dictionary[number] = 1
    else:
        dictionary[number] += 1
print(dictionary)

value = -111
ans = -111
for e in dictionary:
    if dictionary[e] > value:
        value = dictionary[e]
        ans = e

print(ans)

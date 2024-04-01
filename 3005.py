nums = [10,12,11,9,6,19,11]
maximum = 0
entered = 0
count = 0 
dictionary = dict()
visited = []

for element in nums:
    if element not in visited:
        visited.append(element)
        dictionary[element] = 1
    else:
        dictionary[element] += 1

for elements in visited:
    if dictionary[elements] >= maximum:
        maximum = dictionary[elements]

for elements in visited:
    if dictionary[elements] == maximum:
        entered+=1

count = maximum  
count = count*entered
print(dictionary)
print(count)
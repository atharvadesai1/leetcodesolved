def isLongPressedName(name, typed):
    new_typed = typed[0]
    count_typed = []
    count = 1
    for i in range(1, len(typed)):
        if typed[i] == new_typed[-1]:
            count += 1
            continue
        else:
            new_typed+= typed[i]
            count_typed.append(count)
            count = 1
    count_typed.append(count)

    new_name = name[0]
    count_name = []
    count = 1
    for i in range(1, len(name)):
        if name[i] == new_name[-1]:
            count += 1
            continue
        else:
            new_name+= name[i]
            count_name.append(count)
            count = 1
    count_name.append(count)
        
    if new_name != new_typed:
        return False

    for i in range(len(count_name)):
        if count_name[i] <= count_typed[i]:
            continue
        else:
            return False
    
    return True

name = 'atharva'
typed = 'aaathhaarvvvaaa'
ans = isLongPressedName(name, typed)
print(ans)




# remember two conditions:
# 1. Reduce the typed and name string to single element for each repeating dial eg: saeed to saed and
#    saaeeddd to saed
# 2. Also store the frequency of each repeating part and make sure that the frequency of name
#    string is <= typed string 

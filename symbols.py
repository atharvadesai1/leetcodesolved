def isValid(s):
    symbols = {
        '(':')',
        '{':'}',
        '[':']',
        ')': '',
        '}': '',
        ']': '',
    }

    if(len(s)%2==1):
        return False
        
    arr = [ele for ele in s]
    i=0
    while (i<len(arr)-1):
        if(symbols[arr[i]] == arr[i+1]):
            del arr[i:i+2]
            i=0     
            if not arr:
                return True
            continue
        i+=1
    return False

s = input('Enter the symbolic string: ')
val = isValid(s)
print(val)
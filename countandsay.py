def countAndSay(n):
        if n == 1:
            return '1'
        string = '1'
        for _ in range(n-1):
            new_str = ''
            dictionary = dict()
            for i in range(len(string)):
                if string[i] in dictionary:
                    dictionary[string[i]] += 1
                else:
                    dictionary[string[i]] = 1
                
                if i != len(string)-1:
                    if string[i]==string[i+1]:
                        continue
                    else:
                        new_str += str(dictionary[string[i]]) + string[i]
                        dictionary = dict()
                else:
                    new_str +=  str(dictionary[string[i]]) + string[i]

            string = new_str
        return string

ans = countAndSay(7)
print(ans)


#done 
print("Hrrr")
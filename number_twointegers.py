def divide(dividend, divisor):
        ans = 0
        if dividend < divisor:
            return 0
        power_array = []
        temp_div = dividend
        visited = False
        count = 0
        while count < 4:
            count += 1
            i = 0 
            while divisor*pow(2,i) <= temp_div:
                i += 1
                visited = True
            if visited:
                power_array.append(i-1)
                temp_div -= divisor*pow(2,i-1)
                visited = False
            else:
                break
        
        for e in power_array:
             ans += pow(2,e)
        
        return ans

dividend = 768
divisor = 9
ans = divide(dividend, divisor)
print(ans)
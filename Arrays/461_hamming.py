def hammingDistance(x, y):
    count = 0
    x_bin = str(bin(x)[2:])
    y_bin = str(bin(y)[2:])
    if len(x_bin) != len(y_bin):
        if len(x_bin) < len(y_bin):
            while len(x_bin) != len(y_bin):
                x_bin = '0' + x_bin
        else:
            while len(x_bin) != len(y_bin):
                y_bin = '0' + y_bin
    
    for i in range(len(x_bin)):
        if x_bin[i] != y_bin[i]:
            count += 1
    
    return count

ans = hammingDistance(4, 13)
print(ans)

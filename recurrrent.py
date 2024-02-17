n = int(input(('Enter the nth element of pattern: ')))

if(n%10==1 and n%100!=11):
    print(f'The {n}st element of the pattern is {2**(n-1)}')
elif(n%10==2 and n%100!=12):
    print(f'The {n}nd element of the pattern is {2**(n-1)}')
elif(n%10==3 and n%100!=13):
    print(f'The {n}rd element of the pattern is {2**(n-1)}')
else:
    print(f'The {n}th element of the pattern is {2**(n-1)}')
    
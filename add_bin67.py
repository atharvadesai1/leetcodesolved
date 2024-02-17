a = "0"
b = "0"

a_dec = 0
b_dec = 0
for i in range(len(a)):
    if(a[i]=='1'):
        a_dec += 2**(len(a)-1-i)
for i in range(len(b)):
    if(b[i]=='1'):
        b_dec += 2**(len(b)-1-i)

print(f'A dec {a_dec}')
print(f'B dec {b_dec}')

sum = a_dec+b_dec
sum_bin = ''
sum_binr = ''
while(sum!=0):
    sum_bin += str(sum%2)
    sum = sum//2

for char in sum_bin:
    sum_binr = char + sum_binr

print('Sum ', sum_binr)


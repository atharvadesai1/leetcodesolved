solutions = []
def generate_binstring(n,s,i):
    global solutions
    if n==i:
        solutions.append(''.join(s))
        return

    if s[i-1] == '1':
        s[i] = '0'
        generate_binstring(n, s, i+1)
    else:
        s[i] = '0'
        generate_binstring(n, s, i+1)
        s[i] = '1'
        generate_binstring(n, s, i+1)
    
    return

n = 4
s = ['0' for _ in range(n)]
i = 1
solutions = []
generate_binstring(n,s,i)
s[0] = '1'
generate_binstring(n,s,i)
print(solutions)


solutions = []
def paranthesis(s, n, i, brackets):
    if i == n and brackets==0:
        solutions.append(''.join(s))
        return
    elif i == n and brackets!=0:
        return

    if brackets>=0:
        s[i] = ')'
        paranthesis(s, n, i+1, brackets-1)
    if brackets>=0:
        s[i] = '('
        paranthesis(s, n, i+1, brackets+1)
    
    return solutions



n = 3
n *= 2
print(n)
s = ['.' for _ in range(n)]
s[0] = '('
ans = paranthesis(s,n,1,1)
print(ans)

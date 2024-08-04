def dpfibonachi(index, dp):
    if index <= 1:
        return index

    if dp[index] != -1:
        return dp[index]
    dp[index] = dpfibonachi(index-1, dp) + dpfibonachi(index-2, dp)
    return dp[index]

index = int(input("Enter the number: "))
dp = [-1 for _ in range(index)]
ans = dpfibonachi(index-1, dp)
print(ans)


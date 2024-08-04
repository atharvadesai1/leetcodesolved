class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def climbing(total):
            if total < 0:
                return 0
            if total == 0:
                return 1
            if total in memo:
                return memo[total]
            
            memo[total] = climbing(total - 1) + climbing(total - 2)
            return memo[total]
        
        return climbing(n)


sol = Solution()
number = int(input("Enter Number: "))
print(sol.climbStairs(number))
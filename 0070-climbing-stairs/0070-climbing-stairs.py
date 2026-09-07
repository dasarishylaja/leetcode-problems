class Solution:
    def climbStairs(self, n):

        if n <= 2:
            return n

        prev = 1
        curr = 2

        for i in range(3, n + 1):
            new = prev + curr
            prev = curr
            curr = new

        return curr
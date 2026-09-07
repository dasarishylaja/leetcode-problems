class Solution:
    def rob(self, nums):

        if len(nums) == 1:
            return nums[0]

        def rob_line(houses):
            prev = 0
            curr = 0

            for money in houses:
                new = max(curr, prev + money)
                prev = curr
                curr = new

            return curr

        return max(
            rob_line(nums[1:]),
            rob_line(nums[:-1])
        )
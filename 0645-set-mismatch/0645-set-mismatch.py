class Solution:
    def findErrorNums(self, nums):
        n = len(nums)

        for i in range(n):
            index = abs(nums[i]) - 1

            if nums[index] < 0:
                duplicate = abs(nums[i])
            else:
                nums[index] = -nums[index]

        for i in range(n):
            if nums[i] > 0:
                missing = i + 1

        return [duplicate, missing]
class Solution:
    def maxProduct(self, nums):
        current_max = nums[0]
        current_min = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            old_max = current_max
            old_min = current_min

            current_max = max(num, num * old_max, num * old_min)
            current_min = min(num, num * old_max, num * old_min)

            answer = max(answer, current_max)

        return answer
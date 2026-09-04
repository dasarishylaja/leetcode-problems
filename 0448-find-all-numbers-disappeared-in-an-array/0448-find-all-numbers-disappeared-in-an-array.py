class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)

        present = set(nums)

        result = []

        for i in range(1, n + 1):
            if i not in present:
                result.append(i)

        return result
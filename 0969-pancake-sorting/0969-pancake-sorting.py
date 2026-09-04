class Solution:
    def pancakeSort(self, arr):
        result = []
        n = len(arr)

        for size in range(n, 1, -1):
            max_index = arr.index(size)

            # Move the largest number to the front
            if max_index != 0:
                arr[:max_index + 1] = arr[:max_index + 1][::-1]
                result.append(max_index + 1)

            # Move the largest number to its correct position
            arr[:size] = arr[:size][::-1]
            result.append(size)

        return result
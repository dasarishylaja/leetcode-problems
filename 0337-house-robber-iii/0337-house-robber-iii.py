class Solution:
    def rob(self, root):

        def dfs(node):

            if not node:
                return (0, 0)

            left = dfs(node.left)
            right = dfs(node.right)

            # Rob current house
            rob = node.val + left[1] + right[1]

            # Don't rob current house
            skip = max(left) + max(right)

            return (rob, skip)

        return max(dfs(root))
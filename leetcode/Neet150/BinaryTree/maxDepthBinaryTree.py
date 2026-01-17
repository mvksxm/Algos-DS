from TreeNode import TreeNode

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        curr_node = root
        # global max_depth
        max_depth = 0

        def recursive_function(node: TreeNode, cnt: int):
            global max_depth
            if node is None:
                max_depth = max(max_depth, cnt)
                return

            cnt += 1
            recursive_function(node.left, cnt)
            recursive_function(node.right, cnt)

        recursive_function(curr_node,0)

        return max_depth

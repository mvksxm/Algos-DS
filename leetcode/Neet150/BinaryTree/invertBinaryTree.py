from cups import modelSort

from TreeNode import TreeNode

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        if not root:
            return root

        init_node = root
        def recursive_function(node: TreeNode) -> TreeNode | None:
            if node is None or (node.right is None and node.left is None):
                return node

            modified_left = recursive_function(node.left)
            modified_right = recursive_function(node.right)

            node.right = modified_left
            node.left = modified_right

            return node

        new_head = recursive_function(init_node)
        return new_head


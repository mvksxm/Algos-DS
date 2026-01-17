from TreeNode import TreeNode

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        global global_diameter
        global_diameter = 0

        def recursive_function(node: TreeNode):

            global global_diameter

            if not node:
                return 0

            if node.left is None and node.right is None:
                return 1

            left_child_count = recursive_function(node.left)
            right_child_count = recursive_function(node.right)
            global_diameter = max(global_diameter, left_child_count + right_child_count)

            return max(left_child_count, right_child_count) + 1

        init_node = root

        root_max_path = recursive_function(init_node) - 1
        return max(global_diameter, root_max_path)



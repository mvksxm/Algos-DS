from TreeNode import TreeNode

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if not root or not p or not q:
            return None

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root
        # global hm
        # global depth
        # hm = {}
        # init_node = root
        # depth = 1000**3
        #
        # def recursive_func(node, local_depth):
        #     global gm
        #     global depth
        #
        #     is_found = False
        #
        #     if node == p or node == q:
        #         # if local_depth < depth:
        #         #     depth = local_depth
        #         is_found = True
        #
        #
        #
        #
        #     if node.left is None and node.right is None:
        #         return





"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


# My Approach very similar to BFS, will check it later
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> list[int]:
        final_lst = []

        if not root:
            return []

        def traversal(node):
            # if not node.children or len(node.children) == 1:
            #     final_lst.append(node.val)
            #     return
            # [1, 2, 3, 6, 7, 11, 14, ]
            final_lst.append(node.val)

            if not node.children:
                return

            for nd in node.children:
                traversal(nd)

            return

        traversal(root)
        return final_lst

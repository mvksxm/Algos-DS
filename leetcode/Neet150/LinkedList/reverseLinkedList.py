
from ListNode import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        curr_node = head
        prev_node = None

        # 0 -> 1 -> 2 -> 3

        while curr_node != None:
            curr_node_next = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = curr_node_next

        return prev_node

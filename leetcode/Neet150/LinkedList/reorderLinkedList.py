from typing import Optional
from ListNode import ListNode
from tester import Tester

# Time Complexity (Brute Force): O(n**2)
# Space Complexity (Brute Force): O(1)

# Time Complexity (Optimal): O(n)
# Space Complexity (Optimal): O(1)

# Approach
# Create two pointers: quick_pointer and slow_pointer. quick_pointer is supposed to be two times faster than slow_pointer.
# Two pointers are needed in order to get the middle of a linked list and divide it in two. Division, in turn, is needed
# in order to reverse the second part of a list and then to perform an iteration through the first half of a list
# and a reverse one through the second half of a list in parallel. Such iteration would allow to conveniently place items
# from different sides of a list one after another in a newly created Linked List. Head of this new Linked List is supposed
# to be returned.


class Solution:


    def reorderList(self, head: Optional[ListNode]) -> None:

        slow_pointer = head
        quick_pointer = head.next
        res_head = res_node = None

        # Find the middle of a Linked List
        while quick_pointer and quick_pointer.next:
            slow_pointer = slow_pointer.next
            quick_pointer = quick_pointer.next.next

        # Reverse a second portion of a list
        mid_pointer = slow_pointer.next
        slow_pointer.next = None
        mid_prev_pointer = None

        while mid_pointer:
            next_pointer = mid_pointer.next
            mid_pointer.next = mid_prev_pointer
            mid_prev_pointer = mid_pointer
            mid_pointer = next_pointer

        node = head
        reverse_node = mid_prev_pointer

        while reverse_node:
            if not res_node:
                res_node = node
            else:
                res_node.next = node
                res_node = res_node.next

            node = node.next

            res_node.next = reverse_node
            res_node = res_node.next

            reverse_node = reverse_node.next

        while node:
            if not res_node:
                res_node = node
            else:
                res_node.next = node
                res_node = res_node.next

            node = node.next

        if res_head: head = res_head



        # [1, 2, 3, 4]
        # [1, 4, 2, 3]
    #  Brute Force solution
    def reorderListBruteForce(self, head: Optional[ListNode]) -> None:
        node = head
        while node is not None and node.next is not None:
            last_node = self.get_last_node(node)
            next_node = node.next
            node.next = last_node
            node.next.next = next_node
            node = node.next.next

    def get_last_node(self, head):

        node = head

        if node.next is None:
            return node

        while node.next.next is not None:
            node = node.next

        last_node = node.next
        node.next = None
        return last_node



if __name__ == "__main__":
    sln = Solution()
    tst = Tester()

    ## Test 1
    intended_res = [2, 8, 4, 6]
    h = tst.generate_linked_list([2,4,6,8])
    sln.reorderList(h)
    assert tst.decode_linked_list(h) == intended_res

    ## Test 2
    intended_res = [2,10,4,8,6]
    h = tst.generate_linked_list([2,4,6,8,10])
    sln.reorderList(h)
    assert tst.decode_linked_list(h) == intended_res





from ListNode import ListNode
from linkedListOperations import LinkedListOperations
from tester import Tester


# Time Complexity: O(n)
# Space Complexity: O(1)

# Approach
# Create two pointers. One pointer (right) is supposed to have an index bigger than the one of the left pointer on n + 1.
# n + 1, because left pointer is supposed to be pointing to a value right before the element that's supposed to be removed.
# Perform an iteration, after pointers were set up.
# Once right pointer becomes a 'None' value, left pointer's next reference is supposed to be updated to point to the
# left_pointer.next.next. It ensures that the element under left_pointer.next is overridden.

class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        right_pointer = head.next
        left_pointer = head

        cnt = 1
        while cnt < n + 1:

            if not right_pointer:
                return head.next

            right_pointer = right_pointer.next
            cnt += 1


        while right_pointer:
            right_pointer = right_pointer.next
            left_pointer = left_pointer.next

        left_pointer.next = left_pointer.next.next
        return head



    def removeNthFromEndBruteForce(self, head: ListNode, n: int) -> ListNode:
        node = head

        rev_node = rev_head = self._reverse_list(node)
        cnt = 1

        while cnt + 1 < n:
            rev_node = rev_node.next
            cnt += 1

        if n == 1:
            rev_head = rev_head.next
        else:
            rev_node.next = rev_node.next.next

        head = self._reverse_list(rev_head)
        return head

    def _reverse_list(self, n):

        prev_node = None

        while n:
            next_node = n.next
            n.next = prev_node
            prev_node = n
            n = next_node

        return prev_node


if __name__ == "__main__":
    sln = Solution()
    tst = Tester()

    test_cases = [
        [[[1, 2, 3, 4], 2],[1, 2, 4]],
        [[[1, 2], 2],[2]],
        [[[5], 1], None]
    ]

    tst.linked_list_test(test_cases, sln.removeNthFromEnd)


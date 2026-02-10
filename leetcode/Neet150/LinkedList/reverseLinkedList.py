from ListNode import ListNode
from tester import Tester


# Time Complexity: O(n)
# Space Complexity: O(1)

# Approach
# Iterate through the Linked List. On each iteration store the next linked list item in the variable - 'node_next'
# then set the next of the current item to the current 'prev_node' and modify 'prev_node' to store the current item instead.
# Finally, set the current item (var 'node') to 'node_next'. Such operation will be performed until the last element 'node'
# would be reached that has node.next = None. Once this item is reached -> exit the loop, set the curr node's next to the
# current 'prev_node' and return the 'node' itself.

class Solution:
    def reverseList(self, head: ListNode) -> ListNode | None:

        if not head: return None

        prev_node = None
        node = head

        while node.next is not None:
            node_next = node.next
            node.next = prev_node
            prev_node = node
            node = node_next

        node.next = prev_node

        return node

if __name__ == "__main__":
    list_nodes = [0,1,2,3]

    tst = Tester()
    sln = Solution()

    test_cases = [
        [[[0,1,2,3]], [3, 2, 1, 0]]
    ]
    tst.linked_list_test(test_cases, sln.reverseList)
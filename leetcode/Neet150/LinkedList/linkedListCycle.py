from ListNode import ListNode

# Time Complexity: O(n)
# Space Complexity: O(1)

# Approach
# Create a slow pointer and a quick pointer. In case, if at specific time during an iteration, there will be the same
# node present under both of the pointers - return True, because a cycle was detected. In case, if one of the pointers reached
# the None value (end of the list), it means that there is no cycle in the list and False will be returned.

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        if not head: return False

        slow_pointer = head
        quick_pointer = head.next

        while slow_pointer is not None and quick_pointer is not None:

            if slow_pointer == quick_pointer:
                return True

            slow_pointer = slow_pointer.next

            if quick_pointer.next is not None:
                quick_pointer = quick_pointer.next.next
            else:
                return False

        return False
from ListNode import ListNode

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False

        s_p = head
        f_p = head.next

        while s_p is not None and f_p is not None:

            if s_p == f_p:
                return True

            if f_p.next is not None:
                f_p = f_p.next.next
            else:
                return False

            s_p = s_p.next


        return False
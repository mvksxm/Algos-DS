from ListNode import ListNode
from linkedListOperations import LinkedListOperations

class Solution:
    def removeNthFromEnd(head: ListNode, n: int) -> ListNode:

        if not head: return head

        ll_len = 0
        curr_node = head

        while curr_node is not None:
            ll_len += 1
            curr_node = curr_node.next

        target_ind = ll_len - n
        curr_node = head
        curr_index = 0
        prev_node = None
        while curr_node is not None:

            if target_ind == curr_index == 0:
                return head.next

            if target_ind == curr_index:
                prev_node.next = curr_node.next
                return head

            prev_node = curr_node
            curr_node = curr_node.next
            curr_index += 1

        return head

if __name__ == "__main__":
    #-----------------------Test Case #1-----------------------
    elements_list = [1,2,3,4]
    head1 = LinkedListOperations.createLinkedList(elements_list)
    result_head1 = Solution.removeNthFromEnd(head1, 2)
    print(LinkedListOperations.visualizeLinkedList(result_head1))

    #-----------------------Test Case #2-----------------------
    elements_list = [5]
    head1 = LinkedListOperations.createLinkedList(elements_list)
    result_head1 = Solution.removeNthFromEnd(head1, 1)
    print(LinkedListOperations.visualizeLinkedList(result_head1))

    #-----------------------Test Case #3-----------------------
    elements_list = [1,2]
    head1 = LinkedListOperations.createLinkedList(elements_list)
    result_head1 = Solution.removeNthFromEnd(head1, 2)
    print(LinkedListOperations.visualizeLinkedList(result_head1))


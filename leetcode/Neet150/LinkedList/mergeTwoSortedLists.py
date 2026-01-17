from ListNode import ListNode
from linkedListOperations import LinkedListOperations

class Solution:
    def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:


        if list1 is None:
            return list2

        if list2 is None:
            return list1

        curr_node1 = list1
        curr_node2 = list2
        prev_node = None
        head_to_return = None

        while curr_node2 is not None and curr_node1 is not None:

            if curr_node1.val < curr_node2.val:
                if head_to_return is None:
                    head_to_return = curr_node1
                prev_node = curr_node1
                curr_node1 = curr_node1.next

            elif curr_node1.val >= curr_node2.val:
                curr_node2_next = curr_node2.next
                if head_to_return is None:
                    curr_node2.next = curr_node1
                    head_to_return = curr_node2
                    prev_node = curr_node2
                else:
                    prev_node.next = curr_node2
                    prev_node.next.next = curr_node1
                    prev_node = curr_node2

                curr_node2 = curr_node2_next



        if curr_node2 is None and curr_node1 is None:
            return head_to_return

        if curr_node2 is None:
            while curr_node1 is not None:
                prev_node.next = curr_node1
                curr_node1 = curr_node1.next
                prev_node = prev_node.next

        if curr_node1 is None:
            while curr_node2 is not None:
                prev_node.next = curr_node2
                curr_node2 = curr_node2.next
                prev_node = prev_node.next

        return head_to_return

def createLinkedList(elements_list: list):

    pass

if __name__ == "__main__":
    #-----------------------Test Case #1-----------------------
    elements_list1 = [1,2,4]
    head1 = LinkedListOperations.createLinkedList(elements_list1)
    print(LinkedListOperations.visualizeLinkedList(head1))

    elements_list2 = [1,3,5]
    head2 = LinkedListOperations.createLinkedList(elements_list2)
    print(LinkedListOperations.visualizeLinkedList(head2))

    merged_head = Solution.mergeTwoLists(head1, head2)
    print(LinkedListOperations.visualizeLinkedList(merged_head))

    #-----------------------Test Case #2 -----------------------
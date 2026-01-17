from ListNode import ListNode

class LinkedListOperations:

    @staticmethod
    def createLinkedList(elements_list: list):
        if not elements_list:
            return ListNode()

        head = ListNode(elements_list[0])
        prev_node = head

        for i in range(1, len(elements_list)):
            prev_node.next = ListNode(elements_list[i])
            prev_node = prev_node.next

        return head

    @staticmethod
    def visualizeLinkedList(head: ListNode) -> str:

        if not head:
            return ""

        if not head.val and not head.next:
            return ""

        curr_node = head
        linked_list_string = str(head.val)
        curr_node = curr_node.next

        while curr_node is not None:
            linked_list_string += " " + "->" + " " + str(curr_node.val)
            curr_node = curr_node.next

        return linked_list_string
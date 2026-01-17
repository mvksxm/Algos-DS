from ListNode import ListNode
from linkedListOperations import LinkedListOperations

class Solution:

    # Brute Force
    def reorderListBruteForce(head: ListNode) -> None:

        if not head:
            return

        nodes = []
        curr_node = head

        while curr_node is not None:
            nodes.append(curr_node)
            curr_node = curr_node.next

        curr_node = head
        len_nodes = len(nodes)
        idx = 1
        last_node = nodes[len_nodes-idx]

        while curr_node != last_node and curr_node.next != last_node :
            curr_node_next = curr_node.next
            curr_node.next = last_node
            curr_node.next.next = curr_node_next
            curr_node = curr_node.next.next
            idx += 1
            last_node = nodes[len_nodes-idx]

        if curr_node == last_node:
            curr_node.next = None
            return

        last_node.next = None
        curr_node.next = last_node
        return



if __name__ == "__main__":
    elements_list1 = [2,4,6,8,10]
    head1 = LinkedListOperations.createLinkedList(elements_list1)
    Solution.reorderListBruteForce(head1)
    print(LinkedListOperations.visualizeLinkedList(head1))




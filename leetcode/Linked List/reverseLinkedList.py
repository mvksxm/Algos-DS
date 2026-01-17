#  Revert a linked list Iterative Solution

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(n), # O(1) Memory
def revert_linked_list(head):
    node = head
    prev_node = None
    # 2 -> 3 -> 4 -> 5 -> 6
    while node:
        next_node = node.next
        node.next = prev_node
        # try:
        #     print(node.next.val)
        # except:
        #     pass
        prev_node = node
        node = next_node
        # print(node.val)

    return prev_node


if __name__ == "__main__":
    a = [2, 3, 4, 5, 6]
    head = Node(val=2)
    curr_node = head

    i = 1
    while i < len(a):
        curr_node.next = Node(val=a[i])
        curr_node = curr_node.next
        i += 1

    head_of_reverted = revert_linked_list(head)
    print(head_of_reverted.next.next.next.next.val)

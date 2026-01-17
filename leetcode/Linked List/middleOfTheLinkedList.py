class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleOfTheLinkedList(head):
    node = head
    cnt = 0

    while node:
        cnt += 1
        node = node.next

    if cnt % 2 == 0:
        needed_index = cnt / 2
    else:
        needed_index = cnt // 2

    node = head
    # [2, 3, 4, 5, 6]
    while needed_index > 0:
        node = node.next
        needed_index -= 1

    return node


def generateLinkedList():
    a = [3, 1, 2, 3, 4, 5, 6]
    head = Node(val=a[0])
    curr_node = head

    i = 1
    while i < len(a):
        curr_node.next = Node(val=a[i])
        curr_node = curr_node.next
        i += 1

    return head


if __name__ == "__main__":
    head = generateLinkedList()
    print(middleOfTheLinkedList(head).val)

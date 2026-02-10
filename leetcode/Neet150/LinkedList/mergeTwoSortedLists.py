from ListNode import ListNode
from linkedListOperations import LinkedListOperations
from tester import Tester


# Time Complexity: O(n+m), where n -> len(list1), m -> len(list2)
# Space Complexity: O(1). We are not allocating new nodes, just changing next references of each one of them.

# Approach
# Create a dummy head for the new Linked List. Iterate through both of the Linked Lists. On each iteration compare
# elements in each of the list. In case, if one element is less than another one -> iterate the pointer of a list
# with the lower value and add the lower value itself to a result Linked List. After the main iteration, it's highly
# possible that one of the lists that need to be merged, will still have values. In that case, iterate through that list
# and add all  the values that left to the result Linked List. Finally, return the head of a result Linked List.

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        node1 = list1
        node2 = list2

        res_node = res_head = None

        while node1 is not None and node2 is not None:

            next_node = node2

            if node1.val < node2.val:
                next_node = node1
                node1 = node1.next
            else:
                node2 = node2.next

            if res_node is None and res_head is None:
                res_node = res_head = next_node
            else:
                res_node.next = next_node
                res_node = next_node


        while node1 is not None:

            if res_node is None:
                res_node = res_head = node1
            else:
                res_node.next = node1
                res_node = node1

            node1 = node1.next

        while node2 is not None:

            if res_node is None:
                res_node = res_head = node2
            else:
                res_node.next = node2
                res_node = node2

            node2 = node2.next

        return res_head

if __name__ == "__main__":

    sln = Solution()
    tst = Tester()

    test_cases = [
        [[[1,2,4], [1,3,5]],[1,1,2,3,4,5]]
    ]

    tst.linked_list_test(test_cases, sln.mergeTwoLists)
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# Time Complexity (Brute Force / Canonical): O(n) + O(n) = O(n)
# Space Complexity: O(n)

# Approach
# Simple approach here would be to initially create a map with the simple mapping as follows:
# 'Node from the old list' -> 'Newly created Node with the same val as the old one has'. Then, iterate through the old
# list one more time, for each old node extract 'random' and 'next' references, extract new nodes for them from the
# prev created map and assign them to the 'random' and 'next' references of the new node that is mapped to the old one,
# which is currently being processed in the iteration. In the end, return the new node that is mapped to the head of the
# old list, by providing an old head as a key the prev created map.

class Solution:
    def copyRandomListBruteForce(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head: return None

        location_map = {}
        reference_map = {}

        node = head
        idx = 0
        while node:
            location_map[node] = idx
            idx += 1
            node = node.next

        idx = 0
        node = head
        while node:

            if idx in reference_map:
                n_node = reference_map[idx]
            else:
                n_node = Node(node.val)

            if idx > 0:
                prev_node = reference_map[idx - 1]
                prev_node.next = n_node

            old_random_node = node.random
            random_loc = location_map.get(old_random_node, None)

            if random_loc is not None and random_loc not in reference_map:
                if random_loc == idx:
                    reference_map[random_loc] = n_node
                else:
                    reference_map[random_loc] = Node(old_random_node.val)

            if random_loc is not None:
                n_node.random = reference_map[random_loc]

            reference_map[idx] = n_node
            node = node.next
            idx += 1

        return reference_map[0]

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp = {None: None}
        node = head

        while node:
            mp[node] = Node(node.val)
            node = node.next

        node = head
        while node:
            old_random = node.random
            old_next = node.next
            mp[node].random = mp[old_random]
            mp[node].next = mp[old_next]
            node = node.next

        return mp[head]




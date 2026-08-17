"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        tail = dummy
        head2 = head
        rands = {}

        while head:
            tail.next = Node(head.val)
            tail = tail.next
            rands[head] = tail
            head = head.next

        tail2 = dummy.next
        while head2:
            tail2.random = rands.get(head2.random)
            head2 = head2.next
            tail2 = tail2.next
        
        return dummy.next
        
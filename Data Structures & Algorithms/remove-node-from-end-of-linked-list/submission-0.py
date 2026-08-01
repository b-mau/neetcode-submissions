# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        counter = 0
        cur = head
        while cur:
            cur = cur.next
            counter += 1

        prev = dummy
        for _ in range(counter-n):
            prev = prev.next
        prev.next = prev.next.next

        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        if length == n:
            return head.next
        
        prev = head
        for _ in range(length-n-1):
            prev = prev.next
        
        prev.next = prev.next.next

        return head
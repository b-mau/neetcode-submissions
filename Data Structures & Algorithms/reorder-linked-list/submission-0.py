# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle of the list
        mid = self.middleList(head)
        second = mid.next
        mid.next = None

        second = self.reverseList(second)

        first = head
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

    def middleList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev

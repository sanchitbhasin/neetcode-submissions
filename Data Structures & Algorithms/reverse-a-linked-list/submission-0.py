# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        (h, t) = self.reverse(head)
        return h

    def reverse(self, head: Optional[ListNode]) -> (Optional[ListNode], Optional[ListNode]):
        if not head or not head.next:
            return (head, head)
        
        (h, t) = self.reverse(head.next)

        t.next = head
        head.next = None
        return (h, head)

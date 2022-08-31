# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = cur
        while cur and cur.next:
            cur = cur.next
            if cur.val != prev.val:
                prev.next = cur
                prev = cur
        if prev:
            prev.next = None
        return head
        
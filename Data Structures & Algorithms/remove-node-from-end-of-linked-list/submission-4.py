# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head is None:
            return head

        nodes = 0

        curr = head

        while curr:
            nodes += 1
            curr = curr.next

        if n == nodes:
            return head.next 

        idx = 0
        prev = None
        curr = head

        while curr:

            if idx == nodes - n:
                if curr.next:
                    prev.next = curr.next

                else:
                    prev.next = None

            prev = curr
            curr = curr.next

            idx += 1

        return head
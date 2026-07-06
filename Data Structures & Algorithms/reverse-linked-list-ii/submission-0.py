# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if head is None:
            return 

        if left == right:
            return head

        prev = None

        cur = head
        left_prev = None
        left_node = None
        right_node = None
        right_next = None

        id = 0

        while cur:

            id += 1

            if id == left:
                left_prev = prev
                left_node = cur

                prev = cur
                cur = cur.next

                continue

            if id == right:
                right_next = cur.next
                right_node = cur

                right_node.next = prev

                if left_prev:
                    left_prev.next = right_node 
                left_node.next = right_next

                if left > 1:
                    return head

                return right_node

            if left < id < right:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next

            else:
                prev = cur
                cur = cur.next
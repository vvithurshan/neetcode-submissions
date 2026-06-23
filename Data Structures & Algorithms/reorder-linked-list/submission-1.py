# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # if head is None:
        #     return head


        # if head.next is None:
        #     return head

        lst = []

        curr = head

        while curr:
            lst.append(curr)
            curr = curr.next

        curr = ListNode() 
        curr.next = head

        i, j = 0, len(lst) - 1

        while i < j:

            curr.next = lst[i]
            curr = curr.next
            curr.next = lst[j]
            curr = curr.next
            i += 1
            j -= 1

        if i == j:
            curr.next = lst[i]
            curr = curr.next

        curr.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None and list2 is None:
            return None

        if list1 is None:
            return list2

        if list2 is None:
            return list1

        merged = ListNode()
        head = merged
        lst1, lst2 = list1, list2

        while lst1 and lst2:
            if lst1.val <= lst2.val:
                merged.next = lst1
                lst1 = lst1.next

            else:
                merged.next = lst2
                lst2 = lst2.next

            merged = merged.next

        while lst1:
            merged.next = lst1
            lst1 = lst1.next
            merged = merged.next

        while lst2:
            merged.next = lst2
            lst2 = lst2.next
            merged = merged.next

        return head.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ls1 = []
        ls2 = []

        cur = l1
        cur2 = l2

        while cur or cur2:
            if cur:
                ls1.append(str(cur.val))
                cur = cur.next
            else:
                ls1.append(str(0))

            if cur2:
                ls2.append(str(cur2.val))
                cur2 = cur2.next

            else:
                ls2.append(str(0))

        # rem = 0
        # ans = []

        # for i in range(len(ls1) - 1, -1, -1):

        #     val1 = ls1[i]
        #     val2 = ls2[i]

        #     tot = val1 + val2 + rem

        #     if tot // 10 == 0:
        #         ans.append(tot % 10)
        #         rem = 0

        #     else:
        #         rem = 1
        #         ans.append(tot % 10)

        # if rem != 0:
        #     ans.append(rem)

        ans = int("".join(ls1[::-1])) + int("".join(ls2[::-1]))

        ans = list(str(ans))[::-1]


        # ans in a reverse order

        node = ListNode()

        cur = node
        prev = None
        for c in ans:
            cur.val = int(c)
            cur.next = ListNode()
            prev = cur
            cur = cur.next

        prev.next = None

        return node


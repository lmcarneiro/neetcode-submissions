# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        h = {}
        node = head
        i = 0
        while node:
            h[i] = node
            node = node.next
            i += 1
        j = len(h) - n
        print(h)
        print(j)
        if not head.next:
            head = None
        elif j == 0:
            head = head.next
        else:
            if j+1 in h:
                h[j-1].next = h[j+1]
            if j == len(h) - 1:
                h[j-1].next = None
        return head

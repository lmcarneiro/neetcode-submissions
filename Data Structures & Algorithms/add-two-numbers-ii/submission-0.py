# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_list(self, cur):
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        r_l1 = self.reverse_list(l1)
        r_l2 = self.reverse_list(l2)
        carry = 0
        prev = None
        while r_l1 or r_l2 or carry:
            v1 = r_l1.val if r_l1 else 0
            v2 = r_l2.val if r_l2 else 0
            s = str(v1 + v2 + carry)
            carry = 0
            if len(s) > 1:
                carry = int(s[0])
            val = int(s[-1])
            node = ListNode(val, prev)
            prev = node
            r_l1 = r_l1.next if r_l1 else None
            r_l2 = r_l2.next if r_l2 else None
        return prev


    
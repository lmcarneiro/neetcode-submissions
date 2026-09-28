# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        index = 0
        curr = head
        h = {}
        while curr:
            if curr not in h:
                h[curr] = index
            else:
                return True

            curr = curr.next
            index += 1
        return False
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1 = 0
        num2 = 0

        node = l1
        i = 0

        while node:
            num1 += int(node.val * 10**i)
            i += 1
            node = node.next

        node = l2
        i = 0
        
        while node:
            num2 += int(node.val * 10**i)
            i += 1
            node = node.next

        tot = str(num1 + num2)

        nodes = []

        for i in range(len(tot) - 1, -1, -1):
            node = ListNode(int(tot[i]))
            nodes.append(node)
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]

        return nodes[0]
        



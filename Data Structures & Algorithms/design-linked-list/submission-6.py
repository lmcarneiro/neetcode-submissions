class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        cur = self.head.next
        for _ in range(index):
            cur = cur.next
        return cur.val
        
    def addAtHead(self, val: int) -> None:
        new_head = ListNode(val=val)
        new_head.next = self.head.next
        self.head.next = new_head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        # prev_tail = self.tail
        new_tail = ListNode(val=val)
        # if self.tail:
        #     prev_tail.next = self.tail = new_tail
        # else:
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_tail
        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        cur = self.head
        for _ in range(index):
            cur = cur.next
        new_node = ListNode(val=val)
        new_node.next = cur.next
        cur.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        cur = self.head
        
        for _ in range(index):
            cur = cur.next
        cur.next = cur.next.next
        # if index == self.size - 1:
        #     self.tail = cur.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
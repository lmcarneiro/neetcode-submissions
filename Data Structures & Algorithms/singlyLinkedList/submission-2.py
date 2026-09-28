class ListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr and i < index:
            curr = curr.next
            i += 1
        if not curr:
            return -1
        else:
            return curr.value

    def insertHead(self, val: int) -> None:
        new_head = ListNode(val)
        new_head.next = self.head.next
        self.head.next = new_head
        if not new_head.next:
            self.tail = new_head

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next


    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0
        while i < index and curr:
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False


    def getValues(self) -> List[int]:
        curr = self.head.next
        values = []
        while curr:
            values.append(curr.value)
            curr = curr.next
        return values
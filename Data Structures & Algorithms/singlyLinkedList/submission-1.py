class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.dummy_head = Node()
        self.dummy_tail = Node()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.next = self.dummy_head

    
    def get(self, index: int) -> int:
        head = self.dummy_head.next
        curr = head
        i = 0

        while curr != self.dummy_tail and i <= index:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1

        return -1


    def insertHead(self, val: int) -> None:
        head = self.dummy_head.next
        new = Node(val, head)
        self.dummy_head.next = new
        if head == self.dummy_tail:
            self.dummy_tail.next = new


    def insertTail(self, val: int) -> None:
        tail = self.dummy_tail.next
        new = Node(val, self.dummy_tail)
        tail.next = new
        self.dummy_tail.next = new

    def remove(self, index: int) -> bool:
        cur = self.dummy_head

        i = 0
        while cur.next != self.dummy_tail and i <= index:
            if i == index:
                to_del = cur.next
                new_next = to_del.next 
                cur.next = new_next

                if to_del == self.dummy_tail.next:
                    self.dummy_tail.next = cur
                to_del.next = None
                return True
            cur = cur.next
            i += 1

        return False

    def getValues(self) -> List[int]:
        values = []
        cur = self.dummy_head.next

        while cur != self.dummy_tail:
            values.append(cur.val)
            cur = cur.next

        return values

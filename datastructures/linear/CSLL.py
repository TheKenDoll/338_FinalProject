from nodes.SNode import SNode
from SLL import SLL


class CSLL(SLL):
    def __init__(self, head=None):
        super().__init__(head)

    def InsertTail(self, node):
        if not self.head:
            self.head = node
            self.head.SetNext(self.head)
        else:
            current = self.head
            while current.GetNext() != self.head:
                current = current.GetNext()
            current.SetNext(node)
            node.SetNext(self.head)
        self.size += 1

    def Delete(self, node):
        if not self.head:
            return
        if self.head == node:
            if self.head.GetNext() == self.head:
                self.head = None
            else:
                self.head = self.head.GetNext()
            self.size -= 1
            return
        prev = self.head
        current = self.head.GetNext()
        while current != self.head:
            if current == node:
                prev.SetNext(current.GetNext())
                self.size -= 1
                return
            prev = current
            current = current.GetNext()

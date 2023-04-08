from nodes.DNode import DNode
from DLL import DLL

class Queue(DLL):
    def __init__(self):
        super().__init__()

    def enqueue(self, node):
        super().InsertHead(node)

    def dequeue(self):
        if not self.tail:
            return None
        data = self.tail.GetData()
        self.DeleteTail()
        return data

    # Overriding methods with empty bodies
    def InsertTail(self, node):
        pass

    def SortedInsert(self, node):
        pass

    def Insert(self, node, position):
        pass

    def SortedInsert(self, node):
        pass

from nodes.DNode import DNode
from DLL import DLL


class CDLL(DLL):
    def __init__(self, head=None):
        super().__init__(head)
        if self.head:
            self.head.SetPrev(self.tail)
            self.tail.SetNext(self.head)

    def InsertHead(self, node):
        super().InsertHead(node)
        self.head.SetPrev(self.tail)
        self.tail.SetNext(self.head)

    def InsertTail(self, node):
        super().InsertTail(node)
        self.head.SetPrev(self.tail)
        self.tail.SetNext(self.head)

    def Insert(self, node, position):
        super().Insert(node, position)
        self.head.SetPrev(self.tail)
        self.tail.SetNext(self.head)

    def DeleteHead(self):
        super().DeleteHead()
        self.head.SetPrev(self.tail)
        self.tail.SetNext(self.head)

    def DeleteTail(self):
        super().DeleteTail()
        self.head.SetPrev(self.tail)
        self.tail.SetNext(self.head)

    def Delete(self, node):
        if not self.head:
            return
        if node is self.head:
            self.DeleteHead()
        elif node is self.tail:
            self.DeleteTail()
        else:
            node.GetPrev().SetNext(node.GetNext())
            node.GetNext().SetPrev(node.GetPrev())
            self.size -= 1

    def Sort(self):
        if not self.head or self.size <= 1:
            return
        current = self.head.GetNext()
        while current is not self.head:
            temp = current.GetPrev()
            while temp is not self.head.GetPrev() and temp.GetData() > current.GetData():
                temp = temp.GetPrev()
            if temp is not current.GetPrev():
                current.GetPrev().GetNext().SetPrev(current.GetNext())
                current.GetNext().SetPrev(current.GetPrev())
                if temp is self.head:
                    current.SetNext(self.head)
                    self.head.SetPrev(current)
                    self.head = current
                else:
                    current.GetPrev().SetNext(current.GetNext())
                    current.GetNext().SetPrev(current.GetPrev())
                    current.SetNext(temp)
                    temp.SetPrev(current)
                current = current.GetPrev()
            current = current.GetNext()
        self.sorted = True

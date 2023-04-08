from nodes.DNode import DNode


class DLL:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.size = 0
        self.sorted = True

    def InsertHead(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.SetNext(self.head)
            self.head.SetPrev(node)
            self.head = node
        self.size += 1
        self.sorted = False

    def InsertTail(self, node):
        if not self.tail:
            self.head = node
            self.tail = node
        else:
            self.tail.SetNext(node)
            node.SetPrev(self.tail)
            self.tail = node
        self.size += 1
        self.sorted = False

    def Insert(self, node, position):
        if position <= 0:
            self.InsertHead(node)
        elif position >= self.size:
            self.InsertTail(node)
        else:
            current = self.head
            count = 0
            while count < position:
                current = current.GetNext()
                count += 1
            node.SetNext(current)
            node.SetPrev(current.GetPrev())
            current.GetPrev().SetNext(node)
            current.SetPrev(node)
            self.size += 1
            self.sorted = False

    def SortedInsert(self, node):
        if not self.head:
            self.InsertHead(node)
        elif self.sorted and node.GetData() < self.head.GetData():
            self.InsertHead(node)
        elif self.sorted and node.GetData() > self.tail.GetData():
            self.InsertTail(node)
        else:
            current = self.head
            while current.GetNext() and current.GetNext().GetData() < node.GetData():
                current = current.GetNext()
            if current is self.head:
                node.SetNext(self.head)
                self.head.SetPrev(node)
                self.head = node
            else:
                node.SetNext(current.GetNext())
                node.SetPrev(current)
                current.GetNext().SetPrev(node)
                current.SetNext(node)
            self.size += 1

    def Search(self, node):
        current = self.head
        while current:
            if current.GetData() == node.GetData():
                return current
            current = current.GetNext()
        return None

    def DeleteHead(self):
        if not self.head:
            return
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.GetNext()
            self.head.SetPrev(None)
        self.size -= 1

    def DeleteTail(self):
        if not self.tail:
            return
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.GetPrev()
            self.tail.SetNext(None)
        self.size -= 1

    def Delete(self, node):
        current = self.head
        while current:
            if current == node:
                if current is self.head:
                    self.head = current.GetNext()
                    self.head.SetPrev(None)
                elif current is self.tail:
                    self.tail = current.GetPrev()
                    self.tail.SetNext(None)
                else:
                    current.GetPrev().SetNext(current.GetNext())
                    current.GetNext().SetPrev(current.GetPrev())
                self.size -= 1
                return True
            current = current.GetNext()
        return False

    def Sort(self):
        if not self.head:
            return
        sorted = False
        while not sorted:
            sorted = True
            current = self.head
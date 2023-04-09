from nodes.SNode import SNode

class SLL:
    def __init__(self, head=None):
        if head is None:
            self.head = None
        elif isinstance(head, SNode):
            self.head = head
        else:
            raise TypeError("head argument must be an SNode object or None")
            
    def __str__(self):
        nodes = []
        current_node = self.head
        while current_node is not None:
            nodes.append(str(current_node.value))
            current_node = current_node.next
        return "->".join(nodes)


    
    def InsertHead(self, node):
        if not isinstance(node, SNode):
            raise TypeError("node argument must be an SNode object")
        node.next = self.head
        self.head = node
        
    def InsertTail(self, node):
        if not isinstance(node, SNode):
            raise TypeError("node argument must be an SNode object")
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
            
    def Insert(self, node, position):
        if not isinstance(node, SNode):
            raise TypeError("node argument must be an SNode object")
        if position < 0:
            raise ValueError("position argument must be non-negative")
        if position == 0:
            self.InsertHead(node)
        else:
            current_node = self.head
            current_position = 0
            while current_node is not None and current_position < position - 1:
                current_node = current_node.next
                current_position += 1
            if current_node is None:
                raise ValueError("position argument out of range")
            node.next = current_node.next
            current_node.next = node
    
    def SortedInsert(self, node):
        if not isinstance(node, SNode):
            raise TypeError("node argument must be an SNode object")
        if self.head is None or node.value < self.head.value:
            self.InsertHead(node)
        else:
            current_node = self.head
            while current_node.next is not None and node.value > current_node.next.value:
                current_node = current_node.next
            node.next = current_node.next
            current_node.next = node
    
    def __str__(self):
        nodes = []
        current_node = self.head
        while current_node is not None:
            nodes.append(str(current_node.value))
            current_node = current_node.next
        return "->".join(nodes)

    
    def is_empty(self):
        return self.head is None
    
    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.get_next()
        return count
    
    def display(self):
        current = self.head
        while current is not None:
            print(current.get_data(), end=' -> ')
            current = current.get_next()
        print("None")
    
    def insert_head(self, node):
        node.set_next(self.head)
        self.head = node
    
    def insert_tail(self, node):
        if self.is_empty():
            self.insert_head(node)
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(node)
    
    def insert(self, node, position):
        if position == 0:
            self.insert_head(node)
        else:
            current = self.head
            count = 1
            while count < position and current is not None:
                current = current.get_next()
                count += 1
            if current is not None:
                node.set_next(current.get_next())
                current.set_next(node)
            else:
                print("Position out of range.")
    
    def sorted_insert(self, node):
        if self.is_empty() or node.get_data() < self.head.get_data():
            self.insert_head(node)
        else:
            current = self.head
            while current.get_next() is not None and current.get_next().get_data() < node.get_data():
                current = current.get_next()
            node.set_next(current.get_next())
            current.set_next(node)
    
    def search(self, node):
        current = self.head
        while current is not None:
            if current.get_data() == node.get_data():
                return current
            current = current.get_next()
        return None
    
    def delete_head(self):
        if not self.is_empty():
            self.head = self.head.get_next()
    
    def delete_tail(self):
        if not self.is_empty():
            if self.head.get_next() is None:
                self.delete_head()
            else:
                current = self.head
                while current.get_next().get_next() is not None:
                    current = current.get_next()
                current.set_next(None)
    
    def delete(self, node):
        if not self.is_empty():
            if self.head.get_data() == node.get_data():
                self.delete_head()
            else:
                current = self.head
                while current.get_next() is not None and current.get_next().get_data() != node.get_data():
                    current = current.get_next()
                if current.get_next() is not None:
                    current.set_next(current.get_next().get_next())
                else:
                    print("Node not found in the list.")
    
    def sort(self):
        if not self.is_empty() and not self.is_sorted():
            sorted_list = SLL()
            current = self.head
            while current is not None:
                node = SNode(current.get_data())
                sorted_list.sorted_insert(node)
                current = current.get_next()
            self.head = sorted_list.head
    
    def is_sorted(self):
        current = self.head
        while current is not None and current.get_next() is not None:
            if current.get_data() > current.get_next().get_data():
                return False
            current = current.get_next()
        return True

    def Clear(self):
        self.head = None
        self.size = 0
        self.sorted = True

    def Print(self):
        print(f"List length: {self.size}")
        print(f"Sorted status: {'Sorted' if self.sorted else 'Unsorted'}")
        print("List content:")
        current = self.head
        while current:
            print(current.GetData())
            current = current.GetNext()

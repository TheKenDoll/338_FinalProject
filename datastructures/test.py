from nodes.SNode import SNode
from nodes.DNode import DNode
from linear.SLL import SLL
from linear.DLL import DLL
from linear.CSLL import CSLL
from linear.CDLL import CDLL
from linear.StackLL import Stack
from linear.QueueLL import Queue

# Create a singly linked list
sll = SLL()

# Insert some nodes
sll.InsertHead(SNode(1))
sll.InsertTail(SNode(2))
sll.InsertTail(SNode(3))

# Print the list
sll.Print()

# Create a doubly linked list
dll = DLL()

# Insert some nodes
dll.InsertHead(DNode(1))
dll.InsertTail(DNode(2))
dll.InsertTail(DNode(3))

# Print the list
dll.Print()

# Create a circular singly linked list
scll = CSLL()

# Insert some nodes
scll.InsertHead(SNode(1))
scll.InsertTail(SNode(2))
scll.InsertTail(SNode(3))

# Print the list
scll.Print()

# Create a circular doubly linked list
cdll = CDLL()

# Insert some nodes
cdll.InsertHead(DNode(1))
cdll.InsertTail(DNode(2))
cdll.InsertTail(DNode(3))

# Print the list
cdll.Print()

# Create a stack
stack = Stack()

# Push some nodes
stack.push(SNode(1))
stack.push(SNode(2))
stack.push(SNode(3))

# Pop some nodes
print(stack.pop().GetData())
print(stack.pop().GetData())
print(stack.pop().GetData())

# Create a queue
queue = Queue()

# Enqueue some nodes
queue.enqueue(SNode(1))
queue.enqueue(SNode(2))
queue.enqueue(SNode(3))

# Dequeue some nodes
print(queue.dequeue().GetData())
print(queue.dequeue().GetData())
print(queue.dequeue().GetData())

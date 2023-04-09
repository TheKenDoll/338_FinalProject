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

# # Insert some nodes
# sll.InsertHead(SNode(1))
# sll.InsertTail(SNode(5))
# sll.InsertTail(SNode(3))
# sll.InsertHead(SNode(7))
# sll.InsertTail(SNode(99))
# sll.InsertTail(SNode(0))


# # Print the list
# print("SINGLY LINKED LIST")
# sll.Print()
# sll.display()

# Create a doubly linked list
dll = DLL()

# Insert some nodes
dll.InsertHead(DNode(1))
dll.InsertTail(DNode(5))
dll.InsertTail(DNode(3))
dll.InsertTail(DNode(7))
dll.InsertTail(DNode(99))
dll.InsertTail(DNode(0))

# Print the list
print("DOUBLY LINKED LIST")
dll.Print()
dll.display()


# debugging the sort function in DLL, it doesnt seam to be setting the tail to the right thing, so when a function trys to use it then it screws up

print("DOUBLY LINKED LIST")
dll.sort()
dll.Print()
dll.display()
print("HERE")
print(dll.get_tail().get_data())
dll.sorted_insert(DNode(6))
dll.Print()
dll.display()

# # Create a circular singly linked list
# scll = CSLL()

# # Insert some nodes
# scll.InsertHead(SNode(data=1))
# scll.InsertTail(SNode(2))
# scll.InsertTail(SNode(3))

# # Print the list
# print("CIRCULAR SINGLY LINKED LIST")
# scll.Print()
# scll.display()

# # Create a circular doubly linked list
# cdll = CDLL()

# # Insert some nodes
# cdll.InsertHead(DNode(1))
# cdll.InsertTail(DNode(2))
# cdll.InsertTail(DNode(3))

# # Print the list
# print("CIRCULAR DOUBLY LINKED LIST")
# cdll.Print()
# cdll.display()


# # Create a stack
# stack = Stack()

# # Push some nodes
# stack.push(SNode(1))
# stack.push(SNode(2))
# stack.push(SNode(3))

# # Pop some nodes
# print("STACK")
# stack.display()
# print(stack.pop().get_data())
# print(stack.pop().get_data())
# print(stack.pop().get_data())

# # Create a queue
# queue = Queue()

# # Enqueue some nodes

# queue.enqueue(SNode(1))
# queue.enqueue(SNode(2))
# queue.enqueue(SNode(3))

# # Dequeue some nodes
# print("QUEUE")
# queue.display()
# print(queue.dequeue().get_data())
# print(queue.dequeue().get_data())
# print(queue.dequeue().get_data())

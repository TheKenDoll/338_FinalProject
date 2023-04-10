from nodes.SNode import SNode
from nodes.DNode import DNode
from linear.SLL import SLL
from linear.DLL import DLL
from linear.CSLL import CSLL
from linear.CDLL import CDLL
from linear.StackLL import Stack
from linear.QueueLL import Queue

from trees.avl import AVL
from trees.bst import BST
from nodes.TNode import TNode

# Create a singly linked list
sll = SLL()

# Insert some nodes
sll.InsertHead(SNode(1))
sll.InsertTail(SNode(5))
sll.InsertTail(SNode(3))
sll.InsertHead(SNode(7))
sll.InsertTail(SNode(99))
sll.InsertTail(SNode(0))


# Print the list
print("SINGLY LINKED LIST")
sll.Print()
sll.display()
sll.Sort()
sll.SortedInsert(SNode(9))
sll.Print()
sll.display()

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



print("DOUBLY LINKED LIST")
dll.Sort()
dll.SortedInsert(DNode(6))
dll.Print()
dll.display()

# Create a circular singly linked list
scll = CSLL()

# Insert some nodes
scll.InsertHead(SNode(1))
scll.InsertTail(SNode(2))
scll.InsertTail(SNode(3))
scll.InsertTail(SNode(43))
scll.InsertTail(SNode(6))
scll.InsertTail(SNode(99))

# Print the list
print("CIRCULAR SINGLY LINKED LIST")
scll.Print()
scll.display()

print("CIRCULAR SINGLY LINKED LIST")
scll.Sort()
scll.SortedInsert(SNode(5))
scll.Print()
scll.display()

# Create a circular doubly linked list
cdll = CDLL()

# Insert some nodes
cdll.InsertHead(DNode(1))
cdll.InsertTail(DNode(4))
cdll.InsertTail(DNode(96))
cdll.InsertTail(DNode(6))
cdll.InsertTail(DNode(99))
cdll.InsertTail(DNode(68))

# Print the list
print("CIRCULAR DOUBLY LINKED LIST")
cdll.Print()
cdll.display()

print("CIRCULAR DOUBLY LINKED LIST")
cdll.Sort()
cdll.SortedInsert(DNode(10))
cdll.Print()
cdll.display()


# Create a stack
stack = Stack()

# Push some nodes
stack.push(SNode(1))
stack.push(SNode(2))
stack.push(SNode(3))

# Pop some nodes
print("STACK")
stack.display()
print(stack.pop().get_data())
print(stack.pop().get_data())
print(stack.pop().get_data())

# Create a queue
queue = Queue()

# Enqueue some nodes

queue.enqueue(SNode(1))
queue.enqueue(SNode(2))
queue.enqueue(SNode(3))

# Dequeue some nodes
print("QUEUE")
queue.display()
print(queue.dequeue().get_data())
print(queue.dequeue().get_data())
print(queue.dequeue().get_data())

# # Dequeue some nodes
# print("QUEUE")
# queue.display()
# print(queue.dequeue().get_data())
# print(queue.dequeue().get_data())
# print(queue.dequeue().get_data())



# Testing trees
#------------------------------------------

bst = BST()

# bst.insert(10)
# bst.insert(5)
# bst.insert(3)
# bst.insert(7)
# bst.insert(12)
# bst.insert(15)

# bst.printBF()

avl = AVL()

avl.insert(10)
avl.printBF()
input()
avl.insert(11)
avl.printBF()
input()
avl.insert(12)
avl.printBF()
from mylibKIv1.datastructures.nodes.DNode import DNode
from mylibKIv1.datastructures.nodes.SNode import SNode
from mylibKIv1.datastructures.linear.SLL import SLL

from mylibKIv1.datastructures.linear.DLL import DLL
from mylibKIv1.datastructures.linear.CSLL import CSLL
from mylibKIv1.datastructures.linear.CDLL import CDLL
from mylibKIv1.datastructures.linear.StackLL import Stack
from mylibKIv1.datastructures.linear.QueueLL import Queue

from mylibKIv1.datastructures.trees.avl import AVL
from mylibKIv1.datastructures.trees.bst import BST
from mylibKIv1.datastructures.nodes.TNode import TNode



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

# bst.Insert(10)
# bst.Insert(5)
# bst.Insert(3)

# bst.printBF()

# bst.delete(4)

# bst.printBF()


avl = AVL()

# avl.Insert(10)
# avl.printBF()
# input()
# avl.Insert(11)
# avl.printBF()
# input()
# avl.Insert(12)
# avl.printBF()
# input()
# avl.Insert(13)
# avl.printBF()
# input()
# avl.Insert(14)
# avl.printBF()
# input()
# avl.Insert(15)
# avl.printBF()

print("TREE")
bst.Insert(10)
bst.Insert(5)
bst.Insert(3)

bst.printInOrder()

avl.Insert(13)
avl.Insert(14)
avl.Insert(15)

avl.printInOrder()
# AVL tree

from TNode import TNode
from bst import BST

class AVL(BST):

    def __init__(self, root=None) -> None:
        super().__init__(root)

    @classmethod
    def DataAVL(cls, val):
        root = TNode.TNode(val)
        return cls(root)
    
    @classmethod
    def NodeAVL(cls, obj):
        return cls(obj)

    def setRoot(self, node):
        self.root = node
        AVL.rebalance(node)

    def getRoot(self):
        return self.root
    
    def insert(self, input):
        super().insert(input)
        AVL.rebalance(self.root)

    
    def printInOrder(self):
        super().printInOrder()

    def printBF(self):
        super().printBF()

    def rebalance(root):
        # First, build a list of all nodes in the tree in order of increasing depth
        nodes_by_depth = []
        nodes_by_depth.append(set([root]))  # Add the root node
        depth = 0
        while nodes_by_depth[depth]:
            nodes_by_depth.append(set())
            for node in nodes_by_depth[depth]:
                if node.L:
                    nodes_by_depth[depth+1].add(node.L)
                if node.R:
                    nodes_by_depth[depth+1].add(node.R)
            depth += 1
        
        # Next, rebalance each subtree rooted at each node in the tree
        for depth in range(len(nodes_by_depth)-1, -1, -1):
            for node in nodes_by_depth[depth]:
                if node.L and node.R:
                    print("fuck1")
                    if node.balance == -2:
                        if node.R.balance == 1:
                            node.R = AVL.rotate_left(node.R)
                        node = AVL.rotate_right(node)
                    elif node.balance == 2:
                        if node.L.balance == -1:
                            node.L = AVL.rotate_right(node.L)
                        node = AVL.rotate_left(node)
                elif node.L:
                    print("fuck2")
                    if node.balance == -2:
                        node = AVL.rotate_right(node)
                elif node.R:
                    print("fuck3")
                    if node.balance == 2:
                        node = AVL.rotate_left(node)
                if node.P:
                    if node.P.L == node:
                        node.P.L = node
                    else:
                        node.P.R = node
                else:
                    root = node
        
        # Finally, update the balance factors of each node in the tree
        AVL.update_balance_factors(root)

    def rotate_right(node):
        print("cunt")
        new_root = node.L
        node.L = new_root.R
        if new_root.R:
            new_root.R.P = node
        new_root.R = node
        new_root.P = node.P
        node.P = new_root
        node.balance += 1 - min(new_root.balance, 0)
        new_root.balance += 1 + max(node.balance, 0)
        return new_root

    def rotate_left(node):
        print("fuck")
        new_root = node.R
        node.R = new_root.L
        if new_root.L:
            new_root.L.P = node
        new_root.L = node
        new_root.P = node.P
        node.P = new_root
        node.balance += -1 - max(new_root.balance, 0)
        new_root.balance += -1 + min(node.balance, 0)
        return new_root

    def update_balance_factors(node):
        if not node:
            return
        node.balance = AVL.height_of_node(node.R) - AVL.height_of_node(node.L)
        AVL.update_balance_factors(node.L)
        AVL.update_balance_factors(node.R)

    def height_of_node(node):
        if not node:
            return -1
        left_height = AVL.height_of_node(node.L)
        right_height = AVL.height_of_node(node.R)
        return 2 + max(left_height, right_height)

if __name__ == "__main__":
    tree = AVL.DataAVL(10)
    # tree.insert(9)
    # tree.insert(8)
    # tree.insert(7)
    # tree.insert(6)
    # tree.insert(5)
    tree.printBF()
    input()
    tree.insert(11)
    tree.printBF()
    input()
    tree.insert(12)
    tree.printBF()
    input()
    tree.insert(13)
    tree.printBF()
    input()
    tree.insert(14)
    tree.printBF()
    input()
    tree.insert(15)
    tree.printBF()

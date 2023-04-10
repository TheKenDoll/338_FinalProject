# AVL tree

from nodes.TNode import TNode
from trees.bst import BST

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
        AVL.balance_tree(node)

    def getRoot(self):
        return self.root
    
    def insert(self, input):
        super().insert(input)
        AVL.update_balances(self.root)
        AVL.balance_tree(self.root)

    
    def printInOrder(self):
        super().printInOrder()

    def printBF(self):
        super().printBF()

    # def rebalance(root):
    #     # First, build a list of all nodes in the tree in order of increasing depth
    #     nodes_by_depth = []
    #     nodes_by_depth.append(set([root]))  # Add the root node
    #     depth = 0
    #     while nodes_by_depth[depth]:
    #         nodes_by_depth.append(set())
    #         for node in nodes_by_depth[depth]:
    #             if node.L:
    #                 nodes_by_depth[depth+1].add(node.L)
    #             if node.R:
    #                 nodes_by_depth[depth+1].add(node.R)
    #         depth += 1
        
    #     # Next, rebalance each subtree rooted at each node in the tree
    #     for depth in range(len(nodes_by_depth)-1, -1, -1):
    #         for node in nodes_by_depth[depth]:
    #             if node.L and node.R:
    #                 print("fuck1")
    #                 if node.balance == -2:
    #                     if node.R.balance == 1:
    #                         node.R = AVL.rotate_left(node.R)
    #                     node = AVL.rotate_right(node)
    #                 elif node.balance == 2:
    #                     if node.L.balance == -1:
    #                         node.L = AVL.rotate_right(node.L)
    #                     node = AVL.rotate_left(node)
    #             elif node.L:
    #                 print("fuck2")
    #                 if node.balance == -2:
    #                     node = AVL.rotate_right(node)
    #             elif node.R:
    #                 print("fuck3")
    #                 if node.balance == 2:
    #                     node = AVL.rotate_left(node)
    #             if node.P:
    #                 if node.P.L == node:
    #                     node.P.L = node
    #                 else:
    #                     node.P.R = node
    #             else:
    #                 root = node
        
    #     # Finally, update the balance factors of each node in the tree
    #     AVL.update_balance_factors(root)

    # def rotate_right(node):
    #     print("cunt")
    #     new_root = node.L
    #     node.L = new_root.R
    #     if new_root.R:
    #         new_root.R.P = node
    #     new_root.R = node
    #     new_root.P = node.P
    #     node.P = new_root
    #     node.balance += 1 - min(new_root.balance, 0)
    #     new_root.balance += 1 + max(node.balance, 0)
    #     return new_root

    # def rotate_left(node):
    #     print("fuck")
    #     new_root = node.R
    #     node.R = new_root.L
    #     if new_root.L:
    #         new_root.L.P = node
    #     new_root.L = node
    #     new_root.P = node.P
    #     node.P = new_root
    #     node.balance += -1 - max(new_root.balance, 0)
    #     new_root.balance += -1 + min(node.balance, 0)
    #     return new_root

    # def update_balance_factors(node):
    #     if not node:
    #         return
    #     node.balance = AVL.height_of_node(node.R) - AVL.height_of_node(node.L)
    #     AVL.update_balance_factors(node.L)
    #     AVL.update_balance_factors(node.R)

    # def height_of_node(node):
    #     if not node:
    #         return -1
    #     left_height = AVL.height_of_node(node.L)
    #     right_height = AVL.height_of_node(node.R)
    #     return 2 + max(left_height, right_height)


    def balance_tree(node):
        """
        Balances a binary search tree rooted at the given node using the AVL tree balancing technique.
        """
        print(node.print())
        if node.balance > 1:
            print("right")
            # Right heavy, left rotation needed
            print(node.R.balance)
            if node.R.balance > 1:
                # Double rotation needed
                print("fuck")
                node.R = AVL.rotate_right(node.R)
            node = AVL.rotate_left(node)
        elif node.balance < -1:
            print("left")
            # Left heavy, right rotation needed
            if node.L.balance < -1:
                # Double rotation needed
                node.L = AVL.rotate_left(node.L)
            node = AVL.rotate_right(node)
        if node.P is not None:
            AVL.balance_tree(node.P)
        return node


    def rotate_left(node):
        """
        Performs a left rotation on the given node and returns the new root node.
        """
        new_root = node.R
        node.R = new_root.L
        new_root.L = node
        node.balance = node.balance + 1 - min(new_root.balance, 0)
        new_root.balance = new_root.balance + 1 + max(node.balance, 0)
        if node.R is not None:
            node.R.P = node
        new_root.P = node.P
        node.P = new_root
        return new_root


    def rotate_right(node):
        """
        Performs a right rotation on the given node and returns the new root node.
        """
        new_root = node.L
        node.L = new_root.R
        new_root.R = node
        node.balance = node.balance - 1 - max(new_root.balance, 0)
        new_root.balance = new_root.balance - 1 + min(node.balance, 0)
        if node.L is not None:
            node.L.P = node
        new_root.P = node.P
        node.P = new_root
        return new_root
    
    def update_balances(node):
        """
        Recursively updates the balance values for an AVL tree rooted at the given node.
        """
        if node is None:
            return 0
        left_height = AVL.update_balances(node.L)
        right_height = AVL.update_balances(node.R)
        node.balance = right_height - left_height
        return max(left_height, right_height) + 1
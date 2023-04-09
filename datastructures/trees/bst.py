# Binary Search Tree
import TNode

class BST:
    def __init__(self, root=None) -> None:
        self.root = root

    @classmethod
    def DataBST(cls, val):
        root = TNode.TNode(val)
        return cls(root)

    @classmethod
    def NodeBST(cls, obj):
        return cls(obj)
    
    def setRoot(self, newRoot):
        self.root = newRoot

    def getRoot(self):
        return self.root
    
    def insert(self, input):

        if isinstance(input, int):
            new_node = TNode.TNode(input)
        else:
            new_node = input

        height = 0

        if self.root is None:
            self.root = new_node
            return
    
        current_node = self.root

        while True:
            height += 1
            if new_node.data < current_node.data:
                if current_node.L is None:
                    new_node.setP(current_node)
                    new_node.setBalance(height)
                    current_node.L = new_node
                    return
                else:
                    current_node = current_node.L
            elif new_node.data > current_node.data:
                if current_node.R is None:
                    new_node.setP(current_node)
                    new_node.setBalance(height)
                    current_node.R = new_node
                    return
                else:
                    current_node = current_node.R
            else:
                return


    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, cur_node, val):
        if cur_node is None:
            return cur_node

        if val < cur_node.data:
            cur_node.L = self._delete(cur_node.L, val)
        elif val > cur_node.data:
            cur_node.R = self._delete(cur_node.R, val)
        else:
            # Case 1: Node with no children
            if cur_node.L is None and cur_node.R is None:
                cur_node = None
            # Case 2: Node with one child
            elif cur_node.L is None:
                cur_node = cur_node.R
            elif cur_node.R is None:
                cur_node = cur_node.L
            # Case 3: Node with two children
            else:
                temp = self._find_min(cur_node.R)
                cur_node.data = temp.data
                cur_node.R = self._delete(cur_node.R, temp.data)
        return cur_node

    def _find_min(self, cur_node):
        while cur_node.L is not None:
            cur_node = cur_node.L
        return cur_node
            
    def search(self, val):
        return self._search(val, self.root)

    def _search(self, val, cur_node):
        if cur_node is None:
            return TNode.TNode(balance=-1)
        elif cur_node.data == val:
            return cur_node
        elif val < cur_node.data:
            return self._search(val, cur_node.L)
        else:
            return self._search(val, cur_node.R)
        
    # make print out nicer?
    def printInOrder(self):
        self._printInOrder(self.root)

    def _printInOrder(self, cur_node):
        if cur_node is not None:
            self._printInOrder(cur_node.L)
            print(cur_node.data)
            self._printInOrder(cur_node.R)

    # make look nicer?
    def printBF(self):
        if self.root is None:
            return

        cur_level = [self.root]
        while cur_level:
            next_level = []
            for node in cur_level:
                print(node.data, end=" ")
                if node.L:
                    next_level.append(node.L)
                if node.R:
                    next_level.append(node.R)
            print()
            cur_level = next_level

if __name__ == "__main__":
    node1 = BST.DataBST(10)
    print(node1.getRoot().print())
    node1.insert(5)
    node1.insert(7)
    node1.insert(6)
    node1.insert(8)
    node1.insert(11)
    node1.insert(14)
    node1.insert(13)
    node1.printBF()

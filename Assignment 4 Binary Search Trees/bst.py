# bst.py
# ===================================================
# Implement a binary search tree that can store any
# arbitrary object in the tree.
# ===================================================
# https://docs.python.org/3/reference/datamodel.html#object.__lt__

class Student:
    def __init__(self, number, name):
        self.grade = number  # this will serve as the object's key
        self.name = name

    def __lt__(self, kq): #Less than
        return ((self.grade) < (kq))
    
    def __le__(self, kq): #Less than or Eqaul to
        return ((self.grade) <= (kq))

    def __gt__(self, kq): #Greater than
        return ((self.grade) > (kq))
    
    def __ge__(self, kq): #Greater than or Equal to
        return ((self.grade) >= (kq))

    def __eq__(self, kq): #Equal to 
        return ((self.grade) == (kq))
    
    def __ne__(self, kq): #Not Equal to
        return ((self.grade) != (kq))

    def __str__(self): #Return as String value
        if self.grade is not None:
            return str('{self.name}: {self.grade}'.format(self=self))
    # {} is the pointer of the value that must be used by the.format(self=self) function


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val  # when this is a primitive, this serves as the node's key


class BST:
    def __init__(self, start_tree=None) -> None:
        """ Initialize empty tree """
        self.root = TreeNode(None)

        # populate tree with initial nodes (if provided)
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self):
        """
        Traverses the tree using "in-order" traversal
        and returns content of tree nodes as a text string
        """
        values = [str(_) for _ in self.in_order_traversal()]
        return "TREE in order { " + ", ".join(values) + " }"

    def add(self, val):
        """
        Creates and adds a new node to thel BSTree.
        If the BSTree is empty, the new node should added as the root.

        Args:
            val: Item to be stored in the new node
        """

        if self.root.val is None:
            self.root = TreeNode(val)
        else:
            if self.root.val <= val:
                if self.root.right is None:
                    self.root.right = TreeNode(val)
                else:
                    self.addNode(self.root.right, val)
            else:
                if self.root.left is None:
                    self.root.left = TreeNode(val)
                else:
                    self.addNode(self.root.left, val)

    def addNode(self, currentRoot, val):
        """
        Creates and adds a new node to thel BSTree.
        Compare to the add function, this function will add a new root after the main root of the tree
        Therefore, we take a new argument of currentRoot.
        If the val value is smaller than self.root.val, then currentRoot will be self.root.left
        Else it will be self.root.right

        This function is a helper function to help the add function

        Args:
            currentRoot: self.root.(either left or right depends on val value)
            val: Item to be stored in the new node
        """
        if currentRoot.val <= val:
            if currentRoot.right is None:
                currentRoot.right = TreeNode(val)
            else:
                self.addNode(currentRoot.right, val)
        else:
            if currentRoot.left is None:
                currentRoot.left = TreeNode(val)
            else:
                self.addNode(currentRoot.left, val)


    def in_order_traversal(self, cur_node=None, visited=None) -> []:
            """
            Perform in-order traversal of the tree and return a list of visited nodes
            """
            if visited is None:
                # first call to the function -> create container to store list of visited nodes
                # and initiate recursive calls starting with the root node
                visited = []
                self.in_order_traversal(self.root, visited)

            # not a first call to the function
            # base case - reached the end of current subtree -> backtrack
            if cur_node is None:
                return visited

            # recursive case -> sequence of steps for in-order traversal:
            # visit left subtree, store current node value, visit right subtree
            self.in_order_traversal(cur_node.left, visited)
            visited.append(cur_node.val)
            self.in_order_traversal(cur_node.right, visited)
            return visited

    def pre_order_traversal(self, cur_node=None, visited=None) -> []:
        """
        Perform pre-order traversal of the tree and return a list of visited nodes

        Returns:
            A list of nodes in the specified ordering
        """
        if visited is None:
            visited = []
            self.pre_order_traversal(self.root, visited)
        
        if cur_node is None:
            return visited
        
        visited.append(cur_node.val)
        self.pre_order_traversal(cur_node.left,visited)
        self.pre_order_traversal(cur_node.right,visited)
        return visited

    def post_order_traversal(self, cur_node=None, visited=None) -> []:
        """
        Perform post-order traversal of the tree and return a list of visited nodes

        Returns:
            A list of nodes in the specified ordering
        """
        if visited is None:
            visited = []
            self.post_order_traversal(self.root, visited)
        
        if cur_node is None:
            return visited
        
        self.post_order_traversal(cur_node.left, visited)
        self.post_order_traversal(cur_node.right, visited)
        visited.append(cur_node.val)
        return visited

    def contains(self, kq):
        """
        Searches BSTree to determine if the query key (kq) is in the BSTree.

        Args:
            kq: query key

        Returns:
            True if kq is in the tree, otherwise False
        """

        currentRoot = self.root
        while (currentRoot.left is not None or currentRoot.right is not None):
            if currentRoot.val == kq:
                return True
                
            if currentRoot.val > kq:
                currentRoot = currentRoot.left
                if currentRoot is None:
                    return False
                continue

            if currentRoot.val < kq:
                currentRoot = currentRoot.right
                if currentRoot is None:
                    return False
                continue

        if currentRoot.val == kq:
            return True
        else: 
            return False
     

    def left_child(self, node):
        """
        Returns the left-most child in a subtree.

        Args:
            node: the root node of the subtree

        Returns:
            The left-most node of the given subtree
        """

        currentRoot = self.root

        while(currentRoot is not None):
            if currentRoot.val == node:
                while(currentRoot.left is not None):
                    currentRoot = currentRoot.left
                return currentRoot

            if currentRoot.val > node:
                currentRoot = currentRoot.left
                continue

            if currentRoot.val < node:
                currentRoot = currentRoot.right
                continue

    def remove(self, kq):
        """
        Removes node with key k, if the node exists in the BSTree.

        Args:
            node: root of Binary Search Tree
            kq: key of node to remove

        Returns:
            True if k is in the tree and successfully removed, otherwise False
        """
        #FIXME: FIXME Please!

    def get_first(self):
        """
        Gets the val of the root node in the BSTree.

        Returns:
            val of the root node, return None if BSTree is empty
        """
        return self.root.val

    def remove_first(self):
        """
        Removes the val of the root node in the BSTree.

        Returns:
            True if the root was removed, otherwise False
        """
        currentRoot = self.root

        newRootVal = self.leftChild(currentRoot.right.val)

        newRoot = TreeNode(None)

        newRoot.right = currentRoot.right
        newRoot.left = currentRoot.left
        newRoot.val = newRootVal

        self.root = newRoot

        #FIXME: Up to here works, but not below... Alomost

        newRoot = newRoot.right

        while(newRoot.left is not None):
            newRoot = newRoot.left
        
        if newRoot.left is None:
            if newRoot.right is not None:
                newRoot =  newRoot.right
                newRoot.right is None
            
            else:
                newRoot is None

            return True

        else:
            return False







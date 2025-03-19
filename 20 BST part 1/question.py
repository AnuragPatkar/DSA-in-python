# Assignment-20: Binary Search Tree part-1

""" # 1. Define a class Node with instance variables left, item and right. The variables left and right are used to refer left and right child node. The item variable is used to hold data item.
class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right """

""" # 2. Define a class BST to implement Binary Search Tree data structure. Make_init__() method to create root instance variable to hold the reference of root node.
class BST:
    def __init__(self,root=None):
        self.root=root

    def is_empty(self):
        return self.root==None """

""" # 3. In class BST, define insert method to store new data item in the binary search tree.
    def insert(self,data):
        newnode=Node(data)
        if self.is_empty():
            self.root=newnode
        else:
            t=self.root
            while True:
                if data<t.item:
                    if t.left is not None:
                        t=t.left
                    else:
                        t.left=newnode
                        break
                if data>t.item:
                    if t.right is not None:
                        t=t.right
                    else:
                        t.right=newnode
                        break """

""" # 4. In class BST, define a search method to find a given item in the binary search tree and returns the node reference. It returns None if search failed.
    def search(self,data):
        if self.is_empty():
            return None
        t=self.root
        while t is not None:
            if data==t.item:
                return t.item
            if data<t.item:
                t=t.left
            if data>t.item:
                t=t.right
        if t is None:
            return None """

""" # 5. In class BST, define a method to implement inorder traversal.
    def inorder(self):
        def _inorder(node):
            if node:
                _inorder(node.left)
                print(node.item, end=' ')
                _inorder(node.right)
        _inorder(self.root)
        print() """

""" # 6. In class BST, define a method to implement preorder traversal.
    def preorder(self):
        def _preorder(node):
            if node:
                print(node.item, end=' ')
                _preorder(node.left)
                _preorder(node.right)
        _preorder(self.root)
        print() """

""" # 7. In class BST, define a method to implement postorder traversal.
    def postorder(self):
        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                print(node.item, end=' ')
        _postorder(self.root)
        print() """

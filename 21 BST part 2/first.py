class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right

class BST:
    def __init__(self,root=None):
        self.root=root
        self.item_count=0

    def is_empty(self):
        return self.root==None
    
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
                        break
        self.item_count+=1

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
            return None

 
    def preorder(self):
        def _preorder(node):
            if node:
                print(node.item, end=' ')
                _preorder(node.left)
                _preorder(node.right)
        _preorder(self.root)
        print()

    def inorder(self):
        def _inorder(node):
            if node:
                _inorder(node.left)
                print(node.item, end=' ')
                _inorder(node.right)
        _inorder(self.root)
        print()
    
    def postorder(self):
        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                print(node.item, end=' ')
        _postorder(self.root)
        print()

    def minimum(self):
        if self.is_empty():
            return None
        t=self.root
        while t.left is not None:
            t=t.left
        return t.item
    
    def maximum(self):
        if self.is_empty():
            return None
        t=self.root
        while t.right is not None:
            t=t.right
        return t.item

    def delete_item(self, data):
        pass
        

    def size(self):
        return self.item_count
        

b1=BST()
b1.insert(50)
b1.insert(30)
b1.insert(40)
b1.insert(80)
b1.insert(20)
b1.insert(60)
b1.insert(10)
print(b1.search(100))
b1.inorder()
b1.preorder()
b1.postorder()
print(b1.minimum())
print(b1.maximum())
print(b1.size())
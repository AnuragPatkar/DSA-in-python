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
            elif data>t.item:
                t=t.right
            else:
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

    def min_value(self,temp):
        current=temp
        while current.left is not None:
            current=current.left
        return current.item
    
    def max_value(self,temp):
        current=temp
        while current.right is not None:
            current=current.right
        return current.item

    def delete_item(self, data):
        def _delete_node(node, data):
            if node is None:
                return node
            if data < node.item:
                node.left = _delete_node(node.left, data)
            elif data > node.item:
                node.right = _delete_node(node.right, data)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                temp = self.min_value(node.right)
                node.item = temp
                node.right = _delete_node(node.right, temp)
            return node

        self.root = _delete_node(self.root, data)
        self.item_count -= 1

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
print(b1.min_value(b1.root))
print(b1.max_value(b1.root))
print(b1.size())
b1.delete_item(50)
b1.preorder()
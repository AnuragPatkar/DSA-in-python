# Assignment-21: Binary Search Tree part-2

""" # 1. In class BST, define a method to find minimum value item node.
    def min_value(self,temp):
        current=temp
        while current.left is not None:
            current=current.left
        return current.item """

""" # 2. In class BST, define a method to find maximum value item node.
    def max_value(self,temp):
        current=temp
        while current.right is not None:
            current=current.right
        return current.item """

""" # 3. In class BST, define a method to delete a node from binary search tree.
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
        self.item_count -= 1 """

""" # 4. In class BST, define a method size to return the number of elements present in the BST
    def size(self):
        return self.item_count """
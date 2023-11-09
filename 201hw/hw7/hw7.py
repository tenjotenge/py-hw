class TreeNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insert(self, root, key):
        if root is None:
            return TreeNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # Duplicate keys not allowed

        # Update height of the current node
        root.height = 1 + max(self.height(root.left), self.height(root.right))

        # Get the balance factor
        balance = self.balance(root)

        # Perform rotations if necessary
        if balance > 1:
            if key < root.left.key:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        if balance < -1:
            if key > root.right.key:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def insert_key(self, key):
        print(f"Adding {key} to the tree")
        self.root = self.insert(self.root, key)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.key, end=' ')
            self.inorder_traversal(root.right)

    def display(self):
        print("\nAVL Tree:")
        self._display_tree(self.root, 0)
        print("\nInorder traversal:")
        self.inorder_traversal(self.root)
        print("\n")

    def _display_tree(self, node, level):
        if node:
            self._display_tree(node.right, level + 1)
            print("   " * level + f"{node.key} ({node.height})")
            self._display_tree(node.left, level + 1)


# Example usage:
avl_tree = AVLTree()
keys = [10, 20, 30, 40, 50, 25]

print("Adding 10, 20, 30, 40, 50, and 25 to the AVL Tree:")

for key in keys:
    avl_tree.insert_key(key)

print("\nTree after initial insertions:")
avl_tree.display()

# Additional operations
print("Inserting 5 and 15 to the AVL Tree:")
avl_tree.insert_key(5)
avl_tree.insert_key(15)

# Output the final tree
print("\nFinal AVL Tree:")
avl_tree.display()

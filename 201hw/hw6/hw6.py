class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Inorder Tree Traversal - Recursive
def inorder_recursive(root):
    if root:
        inorder_recursive(root.left)
        print(root.val, end=' ')
        inorder_recursive(root.right)

# Inorder Tree Traversal - Non-Recursive (using a stack)
def inorder_non_recursive(root):
    stack = []
    current = root
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.val, end=' ')
            current = current.right
        else:
            break

# Preorder Tree Traversal - Recursive
def preorder_recursive(root):
    if root:
        print(root.val, end=' ')
        preorder_recursive(root.left)
        preorder_recursive(root.right)

# Preorder Tree Traversal - Non-Recursive (using a stack)
def preorder_non_recursive(root):
    stack = [root]
    while stack:
        current = stack.pop()
        if current:
            print(current.val, end=' ')
            stack.append(current.right)
            stack.append(current.left)

# Postorder Tree Traversal - Recursive
def postorder_recursive(root):
    if root:
        postorder_recursive(root.left)
        postorder_recursive(root.right)
        print(root.val, end=' ')

# Postorder Tree Traversal - Non-Recursive (using two stacks)
def postorder_non_recursive(root):
    stack1 = [root]
    stack2 = []
    while stack1:
        current = stack1.pop()
        if current:
            stack2.append(current)
            stack1.append(current.left)
            stack1.append(current.right)
    while stack2:
        node = stack2.pop()
        print(node.val, end=' ')

# Print the original tree
def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        if level == 0:
            print(prefix + str(root.val))
        else:
            print("  " * level + "|-- " + str(root.val))
        if root.left is not None or root.right is not None:
            if root.left is not None:
                print_tree(root.left, level + 1, "L-- ")
            if root.right is not None:
                print_tree(root.right, level + 1, "R-- ")

# Sample Usage
if __name__ == "__main__":
    # Create a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print("Original Tree:")
    print_tree(root)
    print("\n\nInorder Recursive:")
    inorder_recursive(root)
    print("\nInorder Non-Recursive:")
    inorder_non_recursive(root)

    print("\nPreorder Recursive:")
    preorder_recursive(root)
    print("\nPreorder Non-Recursive:")
    preorder_non_recursive(root)

    print("\nPostorder Recursive:")
    postorder_recursive(root)
    print("\nPostorder Non-Recursive:")
    postorder_non_recursive(root)

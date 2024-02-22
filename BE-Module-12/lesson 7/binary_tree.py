class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._find_min_key(root.right)
            root.key = temp.key
            root.right = self._delete_recursive(root.right, temp.key)
        return root

    def _find_min_key(self, node):
        while node.left:
            node = node.left
        return node

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def in_order_traversal(self):
        self._in_order_traversal_recursive(self.root)
        print()

    def _in_order_traversal_recursive(self, node):
        if node:
            self._in_order_traversal_recursive(node.left)
            print(node.key, end=" ")
            self._in_order_traversal_recursive(node.right)

    def pre_order_traversal(self):
        self._pre_order_traversal_recursive(self.root)
        print()

    def _pre_order_traversal_recursive(self, node):
        if node:
            print(node.key, end=" ")
            self._pre_order_traversal_recursive(node.left)
            self._pre_order_traversal_recursive(node.right)

    def post_order_traversal(self):
        self._post_order_traversal_recursive(self.root)
        print()

    def _post_order_traversal_recursive(self, node):
        if node:
            self._post_order_traversal_recursive(node.left)
            self._post_order_traversal_recursive(node.right)
            print(node.key, end=" ")
    
    def print_tree(self):
        self._print_tree_recursive(self.root, 0)

    def _print_tree_recursive(self, node, depth):
        if node is None:
            return
        self._print_tree_recursive(node.right, depth + 1)
        print("    " * depth + str(node.key))
        self._print_tree_recursive(node.left, depth + 1)

# Test the BinaryTree class
if __name__ == "__main__":
    tree = BinaryTree()

    # Insert keys
    keys = [50, 30, 70, 20, 40, 60, 80]
    for key in keys:
        tree.insert(key)

    # In-order traversal
    print("In-order traversal:")
    tree.in_order_traversal()

    # Pre-order traversal
    print("Pre-order traversal:")
    tree.pre_order_traversal()

    # Post-order traversal
    print("Post-order traversal:")
    tree.post_order_traversal()

    print("Binary tree structure:")
    tree.print_tree()

    # Search for a key
    search_key = 40
    if tree.search(search_key):
        print(f"Key {search_key} found in the tree.")
    else:
        print(f"Key {search_key} not found in the tree.")

    # Delete a key
    delete_key = 30
    tree.delete(delete_key)
    print(f"Deleted key: {delete_key}")

    # In-order traversal after deletion
    print("In-order traversal after deletion:")
    tree.in_order_traversal()
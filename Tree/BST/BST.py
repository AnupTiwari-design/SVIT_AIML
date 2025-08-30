class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    elif key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

def search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = find_min(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root

def main():
    root = None
    keys = [50, 30, 20, 40, 70, 60, 80]
    for key in keys:
        root = insert(root, key)

    print("Inorder traversal of BST:")
    inorder(root)

    print("\nSearch 40:", "Found" if search(root, 40) else "Not Found")
    print("Search 25:", "Found" if search(root, 25) else "Not Found")

    print("\nDeleting 20...")
    root = delete(root, 20)
    inorder(root)

    print("\nDeleting 30...")
    root = delete(root, 30)
    inorder(root)

    print("\nDeleting 50...")
    root = delete(root, 50)
    inorder(root)

if __name__ == "__main__":
    main()
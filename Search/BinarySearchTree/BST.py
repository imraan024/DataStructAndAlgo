# Create a node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Inorder traversal
def inorder(root):
    if root is not None:
        # Traverse left
        inorder(root.left)

        # Traverse root
        print(str(root.value) + "->", end=' ')

        # Traverse right
        inorder(root.right)


# Insert a node
def insert(node, value):

    # Return a new node if the tree is empty
    if node is None:
        return Node(value)

    # Traverse to the right place and insert the node
    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)

    return node


# Find the inorder successor
def minValueNode(node):
    current = node

    # Find the leftmost leaf
    while(current.left is not None):
        current = current.left

    return current


# Deleting a node
def deleteNode(root, value):

    # Return if the tree is empty
    if root is None:
        return root

    # Find the node to be deleted
    if value < root.value:
        root.left = deleteNode(root.left, value)
    elif(value > root.value):
        root.right = deleteNode(root.right, value)
    else:
        # If the node is with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # If the node has two children,
        # place the inorder successor in position of the node to be deleted
        temp = minValueNode(root.right)

        root.value = temp.value

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.value)

    return root


root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

print("Inorder traversal: ", end=' ')
inorder(root)

print("\nDelete 7")
root = deleteNode(root, 7)
print("Inorder traversal: ", end=' ')
inorder(root)
print("\nInsert 16")
root = insert(root, 16)
print("Inorder traversal: ", end=' ')
inorder(root)
print("\nDelete 14")
root = deleteNode(root, 14)
print("Inorder traversal: ", end=' ')
inorder(root)

# BST 

class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

# Create a BST
root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)

class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

class BST:
  def __init__(self):
    self.root = None

  def insert(self, key):
    if self.root is None:
      self.root = Node(key)
    else:
      self._insert_recursive(self.root, key)

  def _insert_recursive(self, node, key):
    if key < node.key:
      if node.left is None:
        node.left = Node(key)
      else:
        self._insert_recursive(node.left, key)
    else:
      if node.right is None:
        node.right = Node(key)
      else:
        self._insert_recursive(node.right, key)

  def search(self, key):
    return self._search_recursive(self.root, key)

  def _search_recursive(self, node, key):
    if node is None or node.key == key:
      return node
    if key < node.key:
      return self._search_recursive(node.left, key)
    return self._search_recursive(node.right, key)

  def inorder_traversal(self):
    self._inorder_traversal_recursive(self.root)

  def _inorder_traversal_recursive(self, node):
    if node is not None:
      self._inorder_traversal_recursive(node.left)
      print(node.key)
      self._inorder_traversal_recursive(node.right)

# Create a BST
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

# Perform inorder traversal
bst.inorder_traversal()

class Node:
  def __init__(self, value, left=None, right=None, parent=None):
    self.value = value
    self.left = left
    self.right = right
    self.parent = parent

  def __repr__(self):
    return f"(Value: {self.value}, Left: {self.left}, Right: {self.right})"

def inorder_successor(node):
  if node.right:
    curr = node.right
    while curr.left:
      curr = curr.left
    return curr
  parent = node.parent
  curr = node
  while parent and parent.left is not curr:
    # curr = < span style="color: # 000000" > parent
    parent = parent.parent
  return parent

tree = Node(3)
tree.left = Node(2)
tree.right = Node(4)
tree.left.parent = tree
tree.right.parent = tree
tree.left.left = Node(1)
tree.left.left.parent = tree.left
tree.right.right = Node(5)
tree.right.right.parent = tree.right
#     3
#    / \
#   2   4
#  /     \
# 1       5
print(f"'Left:' {inorder_successor(tree.left)}")
# 3
print(f"'Right:' {inorder_successor(tree.right)}")
# 5
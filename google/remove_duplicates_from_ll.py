class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next
  def __str__(self):
    if not self.next:
      return str(self.val)
    return str(self.val) + " " + str(self.next)

class Solution(object):
  def deleteDuplicates(self, node):
    head = None
    tail = None
    prev = None

    while node:
      if (prev and node.val == prev.val) or (
              node.next and node.val == node.next.val):
        pass
        #duplicate
      else:
        if not head:
          head = node
          tail = head
        else:
          tail.next = node
          tail = node
      prev = node
      node = node.next
    if tail:
      tail.next = None
    return head


n = Node(1, Node(2, Node(3, Node(3, Node(4)))))
print(n)
# 1 2 3 3 4
Solution().deleteDuplicates(n)
print(n)
# 1 2 4



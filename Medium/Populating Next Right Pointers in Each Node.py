"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        self.connect2Nodes(root.left, root.right)
        self.connect(root.left)
        self.connect(root.right)
        return root

    def connect2Nodes(self, root1, root2):
        if root1 == None or root2 == None:
            return
        root1.next = root2
        self.connect2Nodes(root1.right, root2.left)

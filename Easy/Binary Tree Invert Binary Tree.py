def invertTree(self,root):
    if root:
        invert = self.invertTree
        root.left,root.right = invert(root.right),invert(root.left)

        return root


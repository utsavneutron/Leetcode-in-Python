def postOrderTraversal(self,root):
    res = []

    def postOrder(node):
        if node:
            postOrder(node.left)
            postOrder(node.right)
            res.append(node.val)

    postOrder(root)

    return res
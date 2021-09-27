def postOrderTraversal(self,root):
    res = []

    def postOrder(node):
        postOrder(node.left)
        postOrder(node.right)
        res.append(node.val)

    postOrder(root)

    return res
# Recursive Approach
def preorderTraversal(self,node):
    res = []

    def preorder(node):
        res.append(node.val)
        preorder(node.left)
        preorder(node.right)
    
    preorder(root)

    return res



# Iterative Approach
# def preorderTraversal(self,root):
#     stack,res = [],[]

#     if root:
#         stack.append(root)

#     while(stack):
#         root = stack.pop()
#         res.append(root.val)

#         if root.right:
#             stack.append(root.right)
#         if root.left:
#             stack.append(root.left)

#     return res
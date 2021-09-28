def hasPathSum(self,root,targetSum):
    if root == None:
        return False

    if root.left is None and root.right is None and root.val == targetSum:
        return True
    
    return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)
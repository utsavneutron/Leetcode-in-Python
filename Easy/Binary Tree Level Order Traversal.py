def levelOrder(self,root):
    res =[]

    def bfs(root,level):
        if root:
            if len(res) < level:
                res.append([root.val])
            else:
                res.append(root.val)
            
            bfs(root.left,level+1)
            bfs(root.right,level+1)
    
    bfs(root,1)

    return res
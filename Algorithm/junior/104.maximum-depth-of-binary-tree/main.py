def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0   

    if root.left == None:
        return maxDepth(root.right) + 1
    if root.right == None:
        return maxDepth(root.left) + 1
    
    return max(maxDepth(root.left), maxDepth(root.right))+1
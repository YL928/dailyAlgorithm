# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# (╯°□°)╯︵ ǝǝɹʇ ʎɹɐuıq @Max Howell
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        tmp = root.right
        root.right = self.invertTree(root.left)
        root.left = self.invertTree(tmp)
        return root
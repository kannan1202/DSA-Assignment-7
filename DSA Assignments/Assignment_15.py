# Question 2: Invert Binary Tree

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = self.Traverse(root)
        return res

    def Traverse(self,root):
        if root is None:
            return root
        root.left,root.right = root.right,root.left
        root.left = self.Traverse(root.left)
        root.right = self.Traverse(root.right)

        return root
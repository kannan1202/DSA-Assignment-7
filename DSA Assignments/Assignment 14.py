# Question 1: Recover BST:

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        s = self.inorder(root,[])
        for i in range(len(s)):
            if s[i+1].val < s[i].val:
                a = s[i]
                break
        for i in range(len(s)-1,-1,-1):
            if s[i-1].val > s[i].val:
                b = s[i]
                break
        a.val , b.val = b.val, a.val

    def inorder(self,root,s):
        if root is None:
            return s
        s = self.inorder(root.left,s)
        s.append(root)
        s = self.inorder(root.right,s)
        return s
    
# Question 2: Lowest Common Ancestor:

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_val = root.val
        p_val = p.val
        q_val = q.val
        if parent_val < p_val and parent_val < q_val:
            return self.lowestCommonAncestor(root.right,p,q)
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root

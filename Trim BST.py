class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if(root==None):
            return None
        root.left=self.trimBST(root.left,low,high)
        root.right=self.trimBST(root.right,low,high)
        if(root.val<low):
            return root.right
        if(root.val>high):
            return root.left
        return root

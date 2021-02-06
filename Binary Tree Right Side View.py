def right(root,level,height,l):
    if root==None:
        return l
    if level>height[0]:
        l.append(root.val)
        height[0]=level
    right(root.right,level+1,height,l) 
    right(root.left,level+1,height,l)    
    return l
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        l=[]
        return right(root,0,[-1],l)
        

'''
You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

For example, "ab" is lexicographically smaller than "aba".

A leaf of a node is a node that has no children.

TIME -> ON^2 
MEMORY -> ON 
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def smallestFromLeaf(self, root: Optional[TreeNode]) -> str: 
    
    def helper(root, cur): 
        if not root: 
            return 
        
        cur = chr(ord('a') + root.val) + cur
        
        if root.left and root.right:  
            min(helper(root.left, cur), helper(root.right, cur))
        
        if root.right:
            return helper(root.right, cur)
        
        if root.left: 
            return helper(root.left, cur)
        
        return cur
    return helper(root, "")



#Recover Binary Search Tree
class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def insertNode(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.insertNode(val)
            elif val > self.val:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insertNode(val)
            else:
                self.val = val

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.val),
        if self.right:
            self.right.printTree()

    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.val)
            res = res + self.inorderTraversal(root.right)
        return res

    def preOrderTraversal(self, root):
        res = []
        if root:
            res.append(root.val)
            res = res.preOrderTraversal(root.left)
            res = res + self.preOrderTraversal(root.right)
        return res

    def postOrderTraversal(self,root):
        res = []
        if root:
            res = res.postOrderTraversal(root.left)
            res = res + self.postOrderTraversal(root.right)
            res.append(root.val)
        return res

root = TreeNode(20)
root.insertNode(43)
root.insertNode(13)
root.insertNode(10)
root.insertNode(19)
root.insertNode(31)
root.insertNode(42)
print(root.inorderTraversal(root))

# 给定一个二叉树，返回它的 前序 遍历。
# 前序遍历：根-左-右   中序遍历：左-根-右   后序遍历：左-右-根

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import re

class Solution:
    def pre(self,root):
        res=""
        if root!=None:
            res += str(root.val) + "a"
            res += self.pre(root.left) + "a"
            res += self.pre(root.right)
        return res

    def preorderTraversal(self, root: TreeNode):
        res=""
        if root!=None:
            res+=str(root.val)+"a"
            res+=self.pre(root.left)+"a"
            res+=self.pre(root.right)
        temp=re.compile(r"a+")
        return re.sub(temp," ",res).split()


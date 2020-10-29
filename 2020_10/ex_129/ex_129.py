# 给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
#
# 例如，从根到叶子节点路径 1->2->3 代表数字 123。
#
# 计算从根到叶子节点生成的所有数字之和。
#
# 说明: 叶子节点是指没有子节点的节点。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    #递归，对每一个结点判断他的左右儿子结点，自下而上生成子序列列表，最后转int，sum

    def sum(self,root):
        res=[]
        if root==None:
            return res
        else:
            res=[]
            temp_left,temp_right=self.sum(root.left),self.sum(root.right)
            if temp_left==temp_right==[]:
                return [str(root.val)]
            elif temp_left==[]:
                return [str(root.val)+i for i in temp_right]
            elif temp_right==[]:
                return [str(root.val)+i for i in temp_left]
            else:
                for i in temp_left:
                    res.append(str(root.val)+i)
                for j in temp_right:
                    res.append(str(root.val)+j)
                return res

    def sumNumbers(self, root: TreeNode) -> int:
        if root==None:
            return 0
        return sum([int(i) for i in self.sum(root)])

t=Solution()
s1=TreeNode(2)
s1.left=TreeNode(0)
s1.right=TreeNode(0)
print(t.sumNumbers(s1))
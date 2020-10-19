# 给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
#

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(list(map(lambda x:x*x,A)))
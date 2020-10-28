# 给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。
#
# 如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        res=dict()
        for i in arr:
            res[i]=res.get(i,0)+1
        temp=res.values()
        if len(temp)==len(set(temp)):
            return True
        return False
# 给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        nums=set(nums)
        for i in range(1,length+1):
            if i not in nums:
                return i
        return length+1
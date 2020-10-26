class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp=sorted(nums)
        res=[]
        for i in nums:
            res.append(temp.index(i))
        return res
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        current=0
        left=0
        total=sum(nums)
        for i in range(len(nums) ):
            current=nums[i]
            
            
            right_sum=total-left-current
            if left==right_sum:
                return i
            left+=current
        return -1



 
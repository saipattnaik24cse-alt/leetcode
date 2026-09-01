class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sai = set()

        for i in nums:
            if i in sai:
                return True
            else:
                sai.add(i)

        return False
          
           

    

        
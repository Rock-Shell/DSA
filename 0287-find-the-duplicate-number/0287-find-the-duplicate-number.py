class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        s = set()
        for i in nums:
            if i in s:
                return i
            s.add(i)
        
        # nums= sorted(nums)
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return nums[i]
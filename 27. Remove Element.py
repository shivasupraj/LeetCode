class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for k in range(len(nums)):
            if val == nums[i]:
                del nums[i]
            else:
                i += 1
        return len(nums)
        

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        
        info = {}
        for i, num in enumerate(sorted(nums)):
            if num not in info:
                info[num] = i
        return [info[num] for num in nums]
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        cur_ones = 0
        
        for n in nums:
            if n == 1:
                cur_ones += 1
            else:
                max_ones = max(max_ones, cur_ones) 
                cur_ones = 0
                
        return max(max_ones, cur_ones)
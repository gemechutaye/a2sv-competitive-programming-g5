class Solution:
    def numIdenticalPairs(self, nums):
        count = {}
        result = 0

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        for key in count:
            n = count[key]
            result += n * (n - 1) // 2

        return result
class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        num_to_idx = {num:i for i, num in enumerate(nums)}
        
        for old_num, new_num in operations:
            idx = num_to_idx[old_num]
            nums[idx] = new_num
            num_to_idx[new_num] = idx
            del num_to_idx[old_num]
            
        return nums
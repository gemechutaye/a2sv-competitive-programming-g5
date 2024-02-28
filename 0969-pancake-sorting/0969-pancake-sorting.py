class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(arr), 1, -1):
            j = arr.index(max(arr[:i]))
            ans.extend([j + 1, i])
            arr[:j + 1] = arr[:j + 1][::-1]
            arr[:i] = arr[:i][::-1]
        return ans
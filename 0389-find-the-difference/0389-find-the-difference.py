class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        Finds the letter which is missing in s but present in t
        """
        s_count = {}
        t_count = {}

        for ch in s:
            if ch not in s_count:
                s_count[ch] = 0
            s_count[ch] += 1
                
        for ch in t:
            if ch not in t_count: 
                t_count[ch] = 0
            t_count[ch] += 1
        
        for ch in t_count:
            if ch not in s_count or t_count[ch] > s_count[ch]:
                return ch

s = "abcd"
t = "abcde"

sol = Solution()
print(sol.findTheDifference(s, t)) # Prints 'e'
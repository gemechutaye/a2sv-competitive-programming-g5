class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            merged += word1[i] 
            merged += word2[j]
            i += 1
            j += 1
        
        return merged + word1[i:] + word2[j:]
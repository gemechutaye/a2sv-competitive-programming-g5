import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        
        char_count = Counter(s)
        
        max_freq = max(char_count.values())
        
        if max_freq > (n + 1) //2:
            return ''
        
        result = [None] * n
        
        index = 0
        
        for char, freq in char_count.most_common():
            while freq > 0:

                if index >= n:
                    index = 1
                    
                result[index] = char
                
                freq -= 1
                
                index += 2
            
        return ''.join(result)
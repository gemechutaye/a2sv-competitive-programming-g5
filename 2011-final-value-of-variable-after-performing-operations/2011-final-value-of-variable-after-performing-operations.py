class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for op in operations:
            if op == '++X' or op == 'X++':
                x += 1
            elif op == '--X' or op == 'X--':
                x -= 1
        
        return x
        
operations = ["--X","X++","X++"]
print(Solution().finalValueAfterOperations(operations)) # 1

operations = ["++X","++X","X++"] 
print(Solution().finalValueAfterOperations(operations)) # 3

operations = ["X++","++X","--X","X--"]
print(Solution().finalValueAfterOperations(operations)) # 0
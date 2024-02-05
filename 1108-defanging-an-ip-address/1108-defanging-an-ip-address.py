class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged = "" 
        for char in address:
            if char == '.':
                defanged += "[.]" 
            else:
                defanged += char
        return defanged

ip_addr = "1.1.1.1"
solution = Solution() 
print(solution.defangIPaddr(ip_addr))


ip_addr = "255.100.50.0"
print(solution.defangIPaddr(ip_addr))
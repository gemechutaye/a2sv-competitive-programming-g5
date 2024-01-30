class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right+1):
            if '0' not in str(num) and self.isSelfDividing(num):
                result.append(num)
        return result

    def isSelfDividing(self, n: int) -> bool:
        for d in str(n):
            if int(d) == 0 or n % int(d) != 0:
                return False
        return True
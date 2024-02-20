class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        remaining = set(range(1, n+1))
        i = 0
        while len(remaining) > 1:
            i = (i + k - 1) % len(remaining)
            remaining.remove(list(remaining)[i])
        return list(remaining)[0]
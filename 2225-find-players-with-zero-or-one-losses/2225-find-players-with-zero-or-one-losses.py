from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = {}
        losses = {}
        
        # Iterate through matches and count wins and losses for each player
        for winner, loser in matches:
            wins[winner] = wins.get(winner, 0) + 1
            losses[loser] = losses.get(loser, 0) + 1
        
        # Filter players with zero losses
        zero_losses = [player for player in wins.keys() if player not in losses]
        zero_losses.sort()
        
        # Filter players with exactly one loss
        one_loss = [player for player in losses.keys() if losses[player] == 1]
        one_loss.sort()
        
        return [zero_losses, one_loss]

# Example usage:
solution = Solution()
matches1 = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(solution.findWinners(matches1))  # Output: [[1,2,10],[4,5,7,8]]

matches2 = [[2,3],[1,3],[5,4],[6,4]]
print(solution.findWinners(matches2))  # Output: [[1,2,5,6],[]]

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lightest_index = 0
        heaviest_index = len(people) - 1
        boats = 0
        
        while lightest_index <= heaviest_index:
            if people[lightest_index] + people[heaviest_index] <= limit:
                lightest_index += 1
            heaviest_index -= 1
            boats += 1
        
        return boats

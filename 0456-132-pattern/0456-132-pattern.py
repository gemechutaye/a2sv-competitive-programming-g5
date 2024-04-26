class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        #I will initialize vk(valley k) to negative infinity
        vk = -float('inf')

        # I will initialize an empty stack
        stk = []

        # iterate through the array in reverse order
        for x in nums[::-1]:
            # So if the current element in x is smaller than vk,
            # It means there exists a 132 pattern in the array
            if x < vk:
                return True    
            #If the stack is not empty and the top element of the stack
            # is smaller than the current element x
            while stk and stk[-1] < x:
                # Pop elements from the stack and update vk
                # These element can potentially form another third element
                # of a 132 pattern with x as the second element
                vk = stk.pop()

            # push the current elelemt x onto the stack
            stk.append(x)
        
        return False
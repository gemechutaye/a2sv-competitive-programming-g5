class Solution(object):

    def sortColors(self, nums):

        n=len(nums)
 
        lt=-1
        gt=n
        i=0
        while i<gt:
            if nums[i]==1:
                i+=1
            elif nums[i]<1:
                if i!=lt+1:
                    nums[lt+1],nums[i]=nums[i],nums[lt+1]
                lt+=1
                i+=1
            elif nums[i]>1:
                if i!=gt-1:
                    nums[gt-1],nums[i]=nums[i],nums[gt-1]
                gt-=1



if __name__=='__main__':
    
    nums=[2,0,2,1,0,2,1,0]

    solution = Solution()
    solution.sortColors(nums)
    print(nums)
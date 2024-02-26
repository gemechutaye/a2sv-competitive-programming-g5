#User function Template for python3

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        dic = {}
        
        for ele in A:
            if ele in dic:
                dic[ele] += 1
            else:
                dic[ele] = 1
        
        for ele in B:
            if not ele in dic:
                return False
            else:
                dic[ele] -= 1
        
        for ele in dic:
            if dic[ele] != 0:
                return False
        
        return True

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        
        A = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        B = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        ob=Solution()
        if ob.check(A,B,N):
            print(1)
        else:
            print(0)
        
                
                
# } Driver Code Ends
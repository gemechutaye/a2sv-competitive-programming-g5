#User function Template for python3

def isSubset( a1, a2, n, m):
    if len(a2) > len(a1):
        return 'No'
    dic = {}
    
    for ele in a1:
        if ele in dic:
            dic[ele] += 1
        else:
            dic[ele] = 1
    
    for ele in a2:
        if ele not in dic or dic[ele] == 0:
            return 'No'
        else:
            dic[ele] -= 1
    
    return 'Yes'
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
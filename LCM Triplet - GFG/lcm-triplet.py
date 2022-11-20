#User function Template for python3

class Solution:
    def lcmTriplets(self,N):
        #code here
        if N<=2:
            return N
        if (N&1)==1:
            return N*(N-1)*(N-2)
        if N%3==0:
            return (N-2)*(N-1)*(N-3)
        return N*(N-1)*(N-3)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N = int(input())
        ob=Solution()
        print(ob.lcmTriplets(N))
# } Driver Code Ends
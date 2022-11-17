#User function Template for python3
class Solution:


	def countSubarray(self,arr, n, k):

     # code here

     nofsubarrays=(n*(n+1))//2

     count=0

     ans=0

     for v in arr:

         if v<=k:

             count+=1

         elif count>=1:

             ans=ans+((count)*(count+1))//2

             count=0

     ans=ans+((count)*(count+1))//2

     return nofsubarrays-ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n, k=map(int, input().strip().split())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.countSubarray(arr, n, k)
        print(ans)
        tc=tc-1
# } Driver Code Ends
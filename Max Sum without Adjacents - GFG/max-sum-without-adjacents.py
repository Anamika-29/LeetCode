#User function Template for python3
class Solution:

    #Using DP this can complexity can be reduced to O(N)
    def findMaxSum(self, arr, n):
        if n==1: return arr[0]
        if n==2: return max(arr[0], arr[1])

        dp = [-1 for i in range(n)]
        dp[0], dp[1] = arr[0], max(arr[0], arr[1])
        for i in range(2, n): dp[i] = max(dp[i-1], arr[i]+dp[i-2])
        return dp[-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
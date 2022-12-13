class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        dp = A[0]
        for row in A[1:]:
            dp = [value + min([dp[c], dp[max(c - 1, 0)], dp[min(len(A) - 1, c + 1)]]) for c, value in enumerate(row)]
        return min(dp)   
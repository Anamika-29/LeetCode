#User function Template for python3
class Solution:
	def baseEquiv(self, n, m):
		# code here
		for i in range(2,33):
		    if (pow(i,m-1)>n):
		        continue
		    if (pow(i,m)>n):
		        return "Yes"
		return "No"


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,m = input().split()
		n=int(n)
		m=int(m)
		ob = Solution();
		print(ob.baseEquiv(n,m))

# } Driver Code Ends
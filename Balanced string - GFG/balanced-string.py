#User function Template for python3

class Solution:
    def BalancedString(self,N):
        #code here
        li='abcdefghijklmnopqrstuvwxyz'
        n=N//26
        p=N
        ans=li*n
        c=0
        while N>0:
            c+=N%10
            N=N//10
        N=p%26
        if c%2==0:
            if N%2==0:
                ans+=li[:N//2]+li[26-(N//2):26]
            else:
                ans+=li[:(N+1)//2]+li[26-((N-1)//2):26]
        else:
            if N%2==0:
                ans+=li[:N//2]+li[26-(N//2):26]
            else:
                ans+=li[:(N-1)//2]+li[26-((N+1)//2):26]
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        
        ob=Solution()
        print(ob.BalancedString(N))
# } Driver Code Ends
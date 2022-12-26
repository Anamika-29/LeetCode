//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

   class Solution{
public:
    vector<long long>res;
    void precompute()
    {
        // Code Here
        for(int i = 0;i<63;i++){
            for(int j = i+1;j<63;j++){
                for(int k = j+1;k<63;k++){
                        long long num = (1LL<<i)|(1LL<<j)|(1LL<<k);
                        res.push_back(num);
                }
            }
        }
        sort(res.begin(),res.end());
    }
    
    long long solve(long long l, long long r){
        // Code Here
        int L = lower_bound(res.begin(),res.end(),l)-res.begin();    
        int R = upper_bound(res.begin(),res.end(),r)-res.begin();
        return R-L;
    }
    
};




//{ Driver Code Starts.

int main()
{
    int t;
    Solution ob;
    ob.precompute();
    cin>>t;
    while(t--)
    {
        long long l,r;
        cin>>l>>r;
        cout << ob.solve(l, r) << endl; 
    }
    return 0;
}
// } Driver Code Ends
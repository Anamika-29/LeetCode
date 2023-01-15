class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        # each node is a good path
        ans = n
        # sort by vals
        edges.sort(key=lambda x: max(vals[x[0]], vals[x[1]]))
        
        # dsu
        cnt = [1] * n
        root = [i for i in range(n)]
        def get(x):
            # recursively get the root element
            if x == root[x]:
                return x 
            else:
                root[x] = get(root[x])
                return root[x]
        
        # iterate each edge
        for x, y in edges:
            # get the root of x
            x = get(x)
            # get the root of y
            y = get(y)
            # if their vals are same
            if vals[x] == vals[y]:
                # then there would be cnt[x] * cnt[y] good paths
                ans += cnt[x] * cnt[y]
                # unite them
                root[x] = y
                # add the count of x to that of y
                cnt[y] += cnt[x]
            elif vals[x] > vals[y]:
                # unite them
                root[y] = x
            else:
                # unite them
                root[x] = y
        return ans
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        visited = [False]*n
        rows = defaultdict(list)
        cols = defaultdict(list)
        ans = 0
        for i,point in enumerate(stones):
            rows[point[0]].append(i)
            cols[point[1]].append(i)
        
        def dfs(node):
            visited[node] = True
            count = 1
            for x in rows[stones[node][0]]:
                if visited[x] == False:
                    count += dfs(x)
            for x in cols[stones[node][1]]:
                if visited[x] == False:
                    count += dfs(x)
            return count
            
        for i in range(n):
            if visited[i] == False:
                size = dfs(i)
                ans += size-1
        return ans
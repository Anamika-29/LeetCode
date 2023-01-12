class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans = [0] * n
        tree = collections.defaultdict(list)
        for a, b in edges:                             # build tree
            tree[a].append(b)
            tree[b].append(a)
        def dfs(node):                                 # dfs
            nonlocal visited, ans, tree
            c = collections.Counter(labels[node])
            for nei in tree[node]:
                if nei in visited: continue            # avoid revisit
                visited.add(nei)
                c += dfs(nei)                          # add counter (essentially adding a 26 elements dictionary)
            ans[node] = c.get(labels[node])            # assign count of label to this node
            return c
        visited = set([0])
        dfs(0)
        return ans
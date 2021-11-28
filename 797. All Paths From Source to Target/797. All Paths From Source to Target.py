class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        destination = len(graph)-1

        def dfs(path, u):
            if u == destination:
                result.append(path+[u])
            else:
                for v in graph[u]:
                    dfs(path+[u], v)

        dfs([], 0)
        return result

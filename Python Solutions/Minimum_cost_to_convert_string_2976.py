"""
You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters. You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost of changing the character original[i] to the character changed[i].

You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.

Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.

Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].
"""
def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj = defaultdict(list)
        for src, dest, wt in zip(original, changed, cost):
            adj[src].append((dest, wt))
            
        # Solving the problem using Dijkstra's single source shortest path algo
        def dijkstra(src):
            minHeap = []
            heapq.heappush(minHeap, (0, src))
            minCostDict = {}
            minCostDict[src] = 0
            while minHeap:
                cost, node = heapq.heappop(minHeap)
                for nei, wt in adj[node]:
                    if nei not in minCostDict:
                        minCostDict[nei] = 10**10
                    if cost + wt < minCostDict[nei]:
                        heapq.heappush(minHeap, (cost + wt, nei))
                        minCostDict[nei] = cost + wt
            return minCostDict
        
        minCostSrcMap = {c : dijkstra(c) for c in set(source)}
        res = 0
        for src, dst in zip(source, target):
            if dst not in minCostSrcMap[src]:
                return -1
            res += minCostSrcMap[src][dst]
        return res
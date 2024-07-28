"""
2045. Second Minimum Time to Reach Destination

A city is represented as a bi-directional connected graph with n vertices where each vertex is labeled from 1 to n (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself. The time taken to traverse any edge is time minutes.

Each vertex has a traffic signal which changes its color from green to red and vice versa every change minutes. All signals change at the same time. You can enter a vertex at any time, but can leave a vertex only when the signal is green. You cannot wait at a vertex if the signal is green.

The second minimum value is defined as the smallest value strictly larger than the minimum value.

For example the second minimum value of [2, 3, 4] is 3, and the second minimum value of [2, 2, 4] is 4.
Given n, edges, time, and change, return the second minimum time it will take to go from vertex 1 to vertex n.

Notes:

You can go through any vertex any number of times, including 1 and n.
You can assume that when the journey starts, all signals have just turned green.

"""

from collections import defaultdict
class SecondMinTimeToReachDest:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        curr_time = 0
        res = -1
        q = deque([1])
        node_times = defaultdict(list)
        node_times[1] = [curr_time]
        while q:
            for i in range(len(q)):
                curr_node = q.popleft()
                if curr_node == n:
                    if res != -1:
                        return curr_time
                    res = curr_time
                for nei in adj[curr_node]:
                    if len(node_times[nei]) == 0 or (len(node_times[nei]) == 1 and node_times[nei][0] != curr_time):
                        q.append(nei)
                        node_times[nei].append(curr_time)
            if((curr_time // change) % 2 == 1):
                curr_time += change - curr_time % change
            curr_time += time

runner = SecondMinTimeToReachDest()
print(runner.secondMinimum(5, [[1,2],[1,3],[1,4],[3,4],[4,5]], 3, 5))

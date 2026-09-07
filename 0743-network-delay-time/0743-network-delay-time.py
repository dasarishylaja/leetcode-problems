import heapq

class Solution:
    def networkDelayTime(self, times, n, k):

        graph = [[] for _ in range(n + 1)]

        for u, v, w in times:
            graph[u].append((v, w))

        heap = [(0, k)]

        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        while heap:

            time, node = heapq.heappop(heap)

            if time > dist[node]:
                continue

            for next_node, weight in graph[node]:

                new_time = time + weight

                if new_time < dist[next_node]:

                    dist[next_node] = new_time

                    heapq.heappush(
                        heap,
                        (new_time, next_node)
                    )

        answer = max(dist[1:])

        if answer == float('inf'):
            return -1

        return answer
from collections import deque, defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        q = deque()

        freq = defaultdict(int)

        for task in tasks:
            freq[task] += 1

        heap = []

        for task, cnt in freq.items():
            heapq.heappush(heap, (-cnt, task))

        res = 0 
        t = 0

        while heap or q:
            if q and (t - q[0][-1]) == (n + 1):
                cnt, task, _ = q.popleft()
                heapq.heappush(heap, (cnt, task))
            
            if heap:
                cnt, task = heapq.heappop(heap)

                if (cnt + 1) != 0:
                    q.append((cnt+1, task, t))
            
            res += 1

            t += 1

        return res

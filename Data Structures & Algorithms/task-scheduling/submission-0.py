class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        count = Counter(tasks)
        maxH = [-cnt for cnt in count.values()]
        heapq.heapify(maxH)
        q = deque()

        while maxH or q:
            time += 1
            if maxH:
                count = 1 + heapq.heappop(maxH)
                if count:
                    q.append([count, time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxH, q.popleft()[0])
        return time
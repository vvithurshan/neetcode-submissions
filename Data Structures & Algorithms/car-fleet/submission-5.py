class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        n = len(speed)
        stack = []
        pairs = [(position[i], speed[i]) for i in range(n)]
        pairs.sort(reverse=True)

        for pair in pairs:
            time = (target - pair[0]) /  pair[1]
            stack.append(time)

            if len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()

        return len(stack)
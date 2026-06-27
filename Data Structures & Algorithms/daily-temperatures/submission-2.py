class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        ans = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):

            pair = (temp, i)

            while len(stack) > 0 and stack[-1][0] < temp: # mistake I used len(stack) > 1
                T, ind = stack.pop()
                ans[ind] = (i - ind)
            
            stack.append(pair)

        return ans


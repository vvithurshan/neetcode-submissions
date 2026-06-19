class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = []

        for i in range(len(temperatures)):
            ans = 0
            for j in range(i + 1, len(temperatures)):
                
                if temperatures[j] > temperatures[i]:
                    ans = j - i

                    break

            res.append(ans)

        return res
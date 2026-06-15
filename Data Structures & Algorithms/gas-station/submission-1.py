class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        dp = [False] * len(gas)
        bal = 0
        start = 0

        for i in range(len(gas)):
            bal += gas[i]
            if bal - cost[i] >= 0:
                bal -= cost[i]
                dp[i] = True
            else:
                bal = 0
                start = i + 1 if i + 1 < len(gas) else 0

        if sum(dp) == len(gas):
            return start
        for i in range(len(gas)):
            # if start == i:
            #     break
            bal += gas[i]
            if bal - cost[i] >= 0:
                bal -= cost[i]
                dp[i] = True
            else:
                return -1
            
        return start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        PS = []

        for i in range(len(speed)):
            PS.append((position[i], speed[i]))

        PS.sort()

        # (0, 1), (1, 2),  (4, 2), (7, 1)

        # 10, 5, 3, 3

        time = [0] * len(speed)

        for i in range(len(speed)):
            time[i] = (target - PS[i][0])/PS[i][1]


        res = len(position)

        for t in range(len(time) - 2, -1, -1):
            if time[t] <= time[t+1]:
                res -= 1
                time[t] = time[t+1]

        return res
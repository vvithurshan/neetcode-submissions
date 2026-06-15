class Solution:
    def permulation(self, p):
        per = 1
        for i in range(1, p + 1):
            per *= i
        return per

    def climbStairs(self, n: int) -> int:
            if n < 1:
                return 0
            if n == 1:
                return 1
            s = []
            ones = 0
            twos = 0
            ans = 0
            if n % 2:
                s.append(5%2)
                ones += 1
            if n // 2:
                x = n // 2
                for i in range(x):
                    s.append(2)
                    twos += 1
            while len(set(s)) != 1 or set(s) == {2}:
                ans += self.permulation(ones + twos)/(self.permulation(ones) * self.permulation(twos))
                if s[-1] == 2:
                    s.pop()
                    s.append(1)
                    s.append(1)
                    ones += 2
                    twos -= 1
                    s.sort()
            ans += 1
            return int(ans)
                
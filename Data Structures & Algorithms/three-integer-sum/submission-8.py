class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)

        i = 0

        ans = set()

        while i < n - 2:
            j, k = i + 1, n - 1 # mistake I put i + 2

                
            while j < k:
                T = nums[i] + nums[j] + nums[k]

                if T == 0:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

                elif T < 0:
                    j += 1

                else:
                    k -= 1

            i += 1

            while i < n and nums[i] == nums[i - 1]:
                i += 1

        res = list(ans)
        return [list(num) for num in res]

            
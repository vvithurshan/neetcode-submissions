class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = set()
        i = 0 

        while i < len(nums):
            
            j, k = i + 1, len(nums) - 1

            while j < k:
                Sum = nums[i] + nums[j] + nums[k]

                if Sum == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

                elif Sum < 0:
                    j += 1

                else:
                    k -= 1

            i += 1

        ans = []

        for a in res:
            ans.append(list(a))

        return ans
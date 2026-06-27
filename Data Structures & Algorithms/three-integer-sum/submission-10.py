class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        for i, num in enumerate(nums):

            if num > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                T = num + nums[k] + nums[j]

                if T == 0:
                    res.append([num, nums[k], nums[j]])
                    j += 1
                    k -= 1

                    while j < k and (nums[j] == nums[j - 1]):
                        j += 1

                elif T < 0:
                    j += 1

                else:
                    k -= 1

        return res
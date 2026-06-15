class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            tar = 0 - nums[i]
            while l < r:
                curr = nums[l] + nums[r]
                if curr == tar:
                    ans.append([nums[i], nums[l], nums[r]])
                    temp = nums[l]
                    l += 1
                    while l < r and temp == nums[l]:
                        l += 1
                        
                elif curr > tar:
                    r -= 1
                else:
                    l += 1
        return ans

            
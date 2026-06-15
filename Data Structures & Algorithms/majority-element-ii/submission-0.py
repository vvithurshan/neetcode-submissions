class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        count = {}
        ans = []
        for num in nums:
            count[num] = count.get(num, 0) + 1

        threshold = len(nums)/3

        for k, v in count.items():
            if v > threshold:
                ans.append(k)

        return ans
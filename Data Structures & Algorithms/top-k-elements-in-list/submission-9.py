from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict(int)

        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] += 1

        for val, cnt in count.items():

            freq[cnt].append(val)


        ans = []

        for i in range(len(freq) - 1, 0, -1):

            for num in freq[i]:
                ans.append(num)

                if len(ans) == k:
                    return ans
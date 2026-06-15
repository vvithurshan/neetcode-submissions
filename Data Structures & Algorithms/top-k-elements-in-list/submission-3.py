class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        freq_list = []

        for key, val in freq.items():
            freq_list.append((val, key))

        freq_list.sort(key = lambda x : x[0])

        ans = []

        while k:
            top = int(freq_list.pop()[1])
            ans.append(top)
            k -= 1

        return ans
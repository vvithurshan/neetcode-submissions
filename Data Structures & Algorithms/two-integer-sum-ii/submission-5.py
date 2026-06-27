class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        map = {}

        for i in range(len(numbers)):

            find = target - numbers[i]

            if find in map:
                return [map[find], i + 1]

            map[numbers[i]] = i + 1

        return []
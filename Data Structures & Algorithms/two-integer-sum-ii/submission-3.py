class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i, j = 0, len(numbers) - 1

        while i < j:
            T = numbers[i] + numbers[j]

            if T == target:
                return [i + 1, j + 1]

            elif T < target:
                i += 1

            else:
                j -= 1
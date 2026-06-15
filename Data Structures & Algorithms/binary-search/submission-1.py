class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binarySearch(l, r):

            if l > r:
                return -1

            mid = l + (r - l)//2

            if nums[mid] == target:
                return mid

            elif target < nums[mid]:
                return binarySearch(l, mid - 1)

            else:
                return binarySearch(mid + 1, r)

        return binarySearch(0, len(nums) - 1)

        return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binarySearch(l, r, array):

            while l <= r:
                mid = l + (r - l)//2

                if array[mid] == target:
                    return mid

                elif array[mid] < target:
                    l = mid + 1

                else:
                    r = mid - 1

            return - 1

        
        if nums[0] < nums[-1]:
            return binarySearch(0, len(nums) - 1, nums)

        # else
        # 3,5,6,0,1,2

        # index of minimum number

        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l)//2

            if nums[mid] < nums[r]:
                r = mid

            else:
                l = mid + 1

        res = binarySearch(0, l - 1, nums)

        if res != -1:
            return res

        return binarySearch(l, len(nums) - 1, nums)
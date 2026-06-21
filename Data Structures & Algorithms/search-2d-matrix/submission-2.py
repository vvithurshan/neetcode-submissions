class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def bs(array):
            l, r = 0, len(array) - 1

            while l <= r:
                mid = (l + r)//2

                if array[mid] == target:
                    return True

                elif array[mid] < target:

                    l = mid + 1

                else:

                    r = mid - 1

            return False

        
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = (l + r)//2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return bs(matrix[mid])

            elif matrix[mid][0] > target:
                r = mid - 1

            else:
                l = mid + 1

        return False